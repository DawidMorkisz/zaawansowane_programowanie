from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import Query
from fastapi.staticfiles import StaticFiles
import uuid
import os
import glob
import aiofiles
import requests
from api.rabbitmq import publish_task
from api.storage import save_task, get_task

app = FastAPI()

UPLOAD_DIR = "uploads"
PROCESSED_DIR = "processed"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

app.mount("/processed", StaticFiles(directory=PROCESSED_DIR), name="processed")


@app.get("/analyze/path")
async def analyze(path: str = Query(...)):

    if not os.path.exists(path):
        return {"error": "path not found"}

    task_ids = []

    if os.path.isdir(path):
        files = glob.glob(f"{path}/*.[jp][pn]g")
        if not files:
            return {"error": "no image files found in folder"}
        for file_path in files:
            task_id = str(uuid.uuid4())
            save_task(task_id, status="queued")
            publish_task({"task_id": task_id, "image_path": file_path})
            task_ids.append(task_id)
    else:
        task_id = str(uuid.uuid4())
        save_task(task_id, status="queued")
        publish_task({"task_id": task_id, "image_path": path})
        task_ids.append(task_id)

    return {"task_ids": task_ids, "total": len(task_ids)}


@app.get("/analyze/url")
async def analyze_url(image_url: str = Query(...)):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
    except Exception as e:
        return {"error": f"cannot download image: {str(e)}"}

    task_id = str(uuid.uuid4())
    filename = f"{task_id}.jpg"
    file_path = os.path.join(UPLOAD_DIR, filename)

    async with aiofiles.open(file_path, "wb") as f:
        await f.write(response.content)

    save_task(task_id, status="queued")
    publish_task({"task_id": task_id, "image_path": file_path})

    return {"task_id": task_id}


@app.post("/analyze/upload")
async def upload_image(file: UploadFile):
    task_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{task_id}.jpg")

    async with aiofiles.open(file_path, "wb") as f:
        await f.write(await file.read())

    save_task(task_id, status="queued")
    publish_task({"task_id": task_id, "image_path": file_path})

    return {"task_id": task_id}


@app.get("/tasks/{task_id}")
def task_status(task_id: str):
    task = get_task(task_id)
    if not task:
        return {"error": "task not found"}

    result = {"status": task.get("status")}
    if "result" in task:
        result["result"] = task["result"]
        if "processed_image" in task:
            result["processed_image"] = f"/processed/{os.path.basename(task['processed_image'])}"

    if "error" in task:
        result["error"] = task["error"]

    return result
