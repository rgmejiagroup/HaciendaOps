# Adding tasks

The HaciendaOps API lets users add new tasks as mecessary.

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
3. Create the task you want to add, using the existing formatting from the task list. For a list of the tasks currently available in the to-do list, create a new request with the following values:
    * **METHOD**: POST
    * **URL**: `{{base_url}}/task`
    * **Header**: `Content-Type: application/json`
    * **Request Body**:

```json
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
```

4. After creating a new task, create a new request with the following values:
    * **METHOD**: DELETE
    * **URL**: `{{base_url}}/task/{not-in-usetaskId}`
    * **Header**: `Content-Type: application/json`
    * **Request Body**:

```json

{
    "id": 3,
    "title": "Clip weeds",
    "description": "Remove the weeds from Garden C",
    "task_type": "Pruning",
    "due_date": "2024-06-07",
    "completed": false,
    "kaizen_notes": "N/A"
}
```

5. To confirm the task is now on the list, create a request with the following values:
    * **METHOD**: GET
    * **URL**: `{{base_url}}/task/{previoustaskId}`
    * **Header**: `Content-Type: application/json`
    * **Request Body**:

```json

{
    "id": 3,
    "title": "Clip weeds",
    "description": "Remove the weeds from Garden C",
    "task_type": "Pruning",
    "due_date": "2024-06-07",
    "completed": false,
    "kaizen_notes": "N/A"
}
```

6. Postman returns the preceeding response if the task addition was successful.

## Result

You can now locate and add new tasks in HaciendaOps.
