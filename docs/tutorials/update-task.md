# Updating tasks

The HaciendaOps API allows users to update tasks, including the completion status of a task or modifying the due date.

## Prerequisites

* An existing database with tasks
* Access to a command line or Postman
    * This tutorial uses Postman, but can use the command line to make the necessary REST API calls. If using the command line, cURL is necessary to complete
      any API requests.

## Update an existing task

1. Start a local HaciendaOps instance.
   * To start the instance, run the following command:

     ```shell
     cd /HaciendaOps/api
     json-server -w hfg-db.json
     ```

2. Open the Postman app on your computer.
3. For a list of the tasks currently recorded, create a new request with the following values:
    * **METHOD**: GET
    * **URL**: `{{base_url}}/task`
    * **Header**: `Content-Type: application/json`
    * **Return Body**:

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

4. After completing a task, for example, create a new request with the following values:
    * **METHOD**: PATCH
    * **URL**: `{{base_url}}/task/{completetaskId}`
    * **Header**: `Content-Type: application/json`
    * **Request Body**:

      ```json

      {
       "completed": true,
      }
      ```

5. To confirm the task is now complete, create a request with the following values:
    * **METHOD**: GET
    * **URL**: `{{base_url}}/task/{completetaskId}`
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

6. Postman returns the preceeding response if the task modification was successful.

## Result

You can now update existing tasks in HaciendaOps.
