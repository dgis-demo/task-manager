## API implementation
## Authorization
### User registration
`POST /auth/users/`

Description: registers a new user via login and password.

Request body:
```
{
    "username": "user",
    "password": "pass"
}
```
Response:
```
Body:
{
    "email": "",
    "username": "user",
    "id": 1
}
```

### Get authorization token
`POST /auth/token/login/`

Description: gets authorization token for a user

Request body:
```
{
    "username": "user",
    "password": "pass"
}
```
Response:
```
{
    "auth_token": "b424892a281a148e0876d980519a380ed7f3592b"
}
```

`POST /auth/token/logout/`

Description: logs out a user by means of authorization token

Request headers:
```
Authorization: Token b424892a281a148e0876d980519a380ed7f3592b
```

Response:
```
-
```

## Tasks
`GET /api/task_manager/tasks/`

Description: gets all the task belonging to a user

Request headers:
```
Authorization: Token b424892a281a148e0876d980519a380ed7f3592b
```

Response: 
```
[
    {
        "name": "task",
        "description": "Sample task",
        "creation_time": "2020-10-04T19:30:35.875795+03:00",
        "status": "W",
        "planned_completion_date": "2020-12-07"
    }
]
```

`POST /api/task_manager/tasks/`

Description: creates new task

Request headers:
```
Authorization: Token b424892a281a148e0876d980519a380ed7f3592b
```

Request body:
```
{
    "name": "task",
    "description": "Initial task",
    "status": "N",
    "planned_completion_date": "2020-10-05"
}
```

Response:
```
{
    "name": "task",
    "description": "Initial task",
    "creation_time": "2020-10-05T16:49:45.164267+03:00",
    "status": "N",
    "planned_completion_date": "2020-12-05"
}
```

`PUT /api/task_manager/tasks/{task_id}/`

Description: updates task data

Request headers: 
```
Authorization: Token b424892a281a148e0876d980519a380ed7f3592b
```

Request body:
```
{
    "name": "task2",
    "description": "Updated task",
    "status": "W",
    "planned_completion_date": "2020-10-10"
}
```

Response:
```
{
    "name": "task2",
    "description": "Updated task",
    "creation_time": "2020-10-05T16:49:45.164267+03:00",
    "status": "W",
    "planned_completion_date": "2020-12-10"
}
```

`DELETE /api/task_manager/tasks/{task_id}/`

Description: deletes a particular task

Request headers: 
```
Authorization: Token b424892a281a148e0876d980519a380ed7f3592b
```

Response:
```
-
```

### Filtration by status and planned completion date
`GET /api/task_manager/tasks/?status=W&planned_completion_date=2020-12-12`

Description: gets a list of tasks filtered by status and planned completion date

Request headers: 
```
Authorization: Token b424892a281a148e0876d980519a380ed7f3592b
```

Response:
```
[
    {
        "name": "task",
        "description": "Example task",
        "creation_time": "2020-10-06T10:28:17.864311+03:00",
        "status": "W",
        "planned_completion_date": "2020-12-12"
    }
]
```

## History
`GET /api/task_manager/history/`

Description: gets history of all the user's tasks

Request headers: 
```
Authorization: Token b424892a281a148e0876d980519a380ed7f3592b
```

Response:
```
{
    "history": [
        {
            "task1": [
                {
                    "history_date": "10-05-2020, 09:37:45",
                    "name": "task1",
                    "description": "Initial task",
                    "status": "W",
                    "planned_completion_date": "2020-12-19"
                }
            ]
        },
        {
            "task2": [
                {
                    "history_date": "10-05-2020, 13:49:45",
                    "name": "task2",
                    "description": "Simple task",
                    "status": "N",
                    "planned_completion_date": "2020-12-12"
                }
            ]
        }
    ]
}
```

`GET /api/task_manager/history/{task_id}/`

Description: gets history of a particular task

Request headers: 
```
Authorization: Token b424892a281a148e0876d980519a380ed7f3592b
```

Response:
```
{
    "task_history": {
        "task": [
            {
                "history_date": "10-05-2020, 09:37:45",
                "name": "task",
                "description": "Initial task",
                "status": "W",
                "planned_completion_date": "2020-12-19"
            }
        ]
    }
}
```