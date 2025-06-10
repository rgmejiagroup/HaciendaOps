# Deleting tasks

The HaciendaOps API allows users to easily delete existing tasks. For example, this capability can delete tasks after completion
or remove tasks that are no longer relevant.

## Prerequisites

* An existing database with tasks
* Access to a command line or Postman
    * This tutorial uses Postman, but can use the command line to make the necessary REST API calls.

## Deleting an existing task

1. Confirm the local HaciendaOps instance is running.
   * If the service isn't running, run the following command:

     ```shell
     cd <your-github-workspace>/HaciendaOps/api
     json-server -w hfg-db.json

2. Open the Postman app on your computer.
3. Locate the task you want to delete. For a full list of the tasks currently available in the to-do list, create a new request
   with the following values:
    * **METHOD**: GET
    * **URL**: `{{base_url}}/task`
    * **Header**: `Content-Type: application/json`
    * **Request Body**:

    ```
        {   
        "id": 1,
        "title": "Morning irrigation",
        "description": "Water the plants in Garden A",
        "task_type": "Watering",
        "due_date": "2024-06-05",
        "completed": false,
        "kaizen_notes": "Consider shifting to sunrise-only watering to reduce evaporation."
        },
        {
        "id": 2,
        "title": "Apply compost",
        "description": "Use organic compost in Zone B",
        "task_type": "Fertilizing",
        "due_date": "2024-06-06",
        "completed": false
        }

4. After locating the task to delete, create a new request with the following values:
    * **METHOD**: DELETE
    * **URL**: `{{base_url}}/task/{taskId}`
    * **Header**: `Content-Type: application/json`
    * **Request Body**: `{}`
5. To confirm the task isn't on the to-do list, create a request with the following values:
    * **METHOD**: GET
    * **URL**: `{{base_url}}/task/{previoustaskId}`
    * **Header**: `Content-Type: application/json`
    * **Request Body**: `{}`
6. Postman returns the following response if the deletion was successful: `{}` along with a "404 Not Found" error.

## Result

You can now locate and delete existing tasks in HaciendaOps.
