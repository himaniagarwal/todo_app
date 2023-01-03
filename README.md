TODO List application
==================

## Run the application
1. Clone the repo
2. Run  ``docker build . -f dockerfiles/Dockerfile -t todoapp`` 
3. Run ``docker run todoapp -p 80:80``
4. Run ``docker build . -f dockerfiles/Dockerfile-test -t todoapp-test``
5. Run `` docker run todoapp-test ``


### 1. Task creation
Title(maxLength set as 10) is unique for every task \
Supply the data(title, description) in sample.json file \

curl -L -v -H "Content-Type: application/json" -X POST -d @sample.json "http://127.0.0.1:8000/tasks/" \

API will by default mark the task as "incomplete"

### 2. Get all tasks
Displays list of all the tasks (Title, Description, Completion status) \
curl -v -L "http://127.0.0.1:8000/tasks"

### 3. Get task by title
Get the task by its title \
curl -v -L  "http://127.0.0.1:8000/tasks?title="title""

### 4.  Get task by task id
Get the task by it's task id \
curl -v -L  "http://127.0.0.1:8000/tasks?task_id={task_id}"

### 5. Search task by multiple terms
Search task(or tasks) by multiple search terms in description 
curl  -v -L "http://127.0.0.1:8000/tasks/search?q=abc&q=def" 

### 6. Update task by title (edit title, edit description, mark task as completed )
curl -L -v -H "Content-Type: application/json" -X PATCH -d @sample.json "http://127.0.0.1:8000/tasks/{task_id}" \
``sample.json``: \
{ "title" : " Updated title"} \
OR \
{"description": "updated description"} \
OR \
{ "title" : " Updated title" \
"description": "updated description"} \
OR \
{"completed": true} 

### 7. Delete task by task id
 curl -X "DELETE"  "http://127.0.0.1:8000/tasks/{task_id}"  
 

### 8. DB operations
sqlite3 \
.open sql_app.db \
.tables \
select * from tasks; \
