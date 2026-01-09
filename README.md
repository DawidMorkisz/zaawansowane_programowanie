## People Counter API

### Start
docker-compose up --scale worker=5

### RabbitMQ
http://localhost:15672
guest / guest

### API
POST /analyze/upload
GET  /tasks/{task_id}
