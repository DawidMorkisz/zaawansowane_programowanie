## People Counter API

### Start
Keep in mind that have to run docker desktop first
Navigate via terminal to "people-counter" folder then run this command in the terminal. 
Number of workers can be modified, the more worker will be running the more CPU will be used.

docker compose up --scale worker=1

for older docker versions if this command doesn't work try:

docker-compose up --scale worker=1


### Swagger
http://localhost:8000/docs

### RabbitMQ
http://localhost:15672
guest / guest
 

### API
Go to the swagger site to test the endpoints
all of the endpoints can be tested as follows

1. GET  /analyze/path{path}
to this endpoing you can either paste a path to single png/jpg file or to the whole folder.
if providing path to folder, the app will process every png/jpg file in it.
for the test purpose there is a folder with over 1000 images to test it called "Images".
Remember that the folder/image must be in the "people-counter" folder to work
for example to prosess all 1000 images the path will be 
/app/Images

for single file  /app/Images/{filename} 

2. GET  /analyze/url{image url}
Find a image on the internet, "Right-click" on it then choose "Copy Image Address"
and just paste it after the url

3. POST /analyze/upload

after clicking uplad image button the file explorer apear, choose desired image to begin processing

4. GET  /tasks/{task_id}
you can check current status of desired pending process by pasting here its ID (Id is given in response for every image that you put in the queue).


All of the processed images will apear in the "processed" folder.


To turn of the app 
mouse-click on the terminal , then press Ctrl+C and now press any button on keyboard, 
Other way to stop the app is opening new terminal and executing command below
docker compose down

DISCLAIMER
This app uses simple HOG algorithm, its not the best,
often make mistakes even after changing parameters.
Since YOLO took to much of my machine resources this is the best I could do.
