from fastapi import FastAPI, UploadFile, Query
import uuid
import os
import aiofiles
import aiohttp
import glob

from api.rabbitmq import publish_task
from api.storage import save_task, get_task

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/analyze/upload")
async def upload_image(file: UploadFile):
    task_id = str(uuid.uuid4())
    path = f"{UPLOAD_DIR}/{task_id}.jpg"

    async with aiofiles.open(path, "wb") as f:
        await f.write(await file.read())

    save_task(task_id, status="queued")
    publish_task({"task_id": task_id, "image_path": path})

    return {"task_id": task_id}


@app.get("/analyze/folder")
async def analyze_folder(folder_path: str = Query(...)):
    """
    Kolejkuje wszystkie zdjęcia z podanego folderu.
    """
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        return {"error": "folder not found"}

    task_ids = []

    for file_path in glob.glob(f"{folder_path}/*.[jp][pn]g"):
        task_id = str(uuid.uuid4())
        save_task(task_id, status="queued")
        publish_task({"task_id": task_id, "image_path": file_path})
        task_ids.append(task_id)

    return {"task_ids": task_ids, "total": len(task_ids)}


@app.get("/analyze/url")
async def analyze_url(url: str = Query(...)):
    task_id = str(uuid.uuid4())
    path = f"{UPLOAD_DIR}/{task_id}.jpg"

    # pobranie obrazu z Internetu asynchronicznie
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return {"error": "failed to download image"}
            content = await resp.read()

    async with aiofiles.open(path, "wb") as f:
        await f.write(content)

    save_task(task_id, status="queued")
    publish_task({"task_id": task_id, "image_path": path})

    return {"task_id": task_id}


@app.get("/tasks/{task_id}")
def task_status(task_id: str):
    task = get_task(task_id)
    if not task:
        return {"error": "task not found"}
    return task
