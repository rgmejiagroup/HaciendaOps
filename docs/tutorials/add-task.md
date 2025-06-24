# Adding tasks

The HaciendaOps API lets users add new tasks as necessary.

## Prerequisites

* An existing database with tasks
* Access to a command line or Postman
    * This tutorial uses Postman, but can use the command line to make the necessary REST API calls. If using the command line, cURL is necessary to complete
      any API requests.

## Add a new task

1. Start a local HaciendaOps instance.
   * To start the instance, run the following command:

     ```shell
     cd /HaciendaOps/api
     json-server -w hfg-db.json
     ```

1. Open the Postman app on your computer.
1. View a list of the tasks currently recorded using a request with the following values:
    * **METHOD**: GET
    * **URL**: `{{base_url}}/task`
    * **Header**: `Content-Type: application/json`
    * **Response Body**:

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

1. Create the task you want to add, using the existing formatting from the task list. After creating a new task, create a new request with the following values:
    * **METHOD**: POST
    * **URL**: `{{base_url}}/task/{newtaskId}`
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

1. To confirm the task is now on the list, create a request with the following values:
    * **METHOD**: GET
    * **URL**: `{{base_url}}/task/{newtaskId}`
    * **Header**: `Content-Type: application/json`
    * **Response Body**:

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

1. Postman returns the preceeding response if the task addition was successful.

## Result

You can now locate and add new tasks in HaciendaOps.
