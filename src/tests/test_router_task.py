import string
import sys
import random

sys.path.append('../todoapp')

from fastapi.testclient import TestClient
from todoapp.main import app
from todoapp.config.database import create_tables

create_tables()
client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to todo list application"}


def test_200_create_task():
    title = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    data = {
        "title": title,
        "description": "Test description"
    }
    response = client.post("/tasks/", json=data)
    print("printing the ************************@@@@@@@")
    print(response.json())
    assert response.status_code == 200
    assert response.json()["success"] is True


def test_422_create_task_without_title():
    data = {
        "description": "Test title"
    }
    response = client.post("/tasks/", json=data)
    assert response.status_code == 422


def test_422_create_task_without_description():
    data = {
        "title": "Test title"
    }
    response = client.post("/tasks/", json=data)
    assert response.status_code == 422


def test_404_get_task():
    response = client.get("/tasks?task_id=100")
    assert response.status_code == 200
    assert response.json()["success"] is False


def test_delete_task():
    response = client.delete("/tasks/2")
    assert response.status_code == 200
