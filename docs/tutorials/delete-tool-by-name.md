# Deleting tools

The HaciendaOps API allows users to delete existing tools, should something break during work or is no longer needed in the "toolbox."
or remove tasks that are no longer relevant.

## Prerequisites

* An existing database with tasks
* Access to a command line or Postman
    * This tutorial uses Postman, but can use the command line to make the necessary REST API calls.

## Deleting an existing tool

1. Confirm the local HaciendaOps instance is running.
   * If the service isn't running, run the following command:

     ```shell
     cd <your-github-workspace>/HaciendaOps/api
     json-server -w hfg-db.json

2. Open the Postman app on your computer.
3. Locate the task you want to delete. For a full list of the tasks currently available in the to-do list, create a new request
   with the following values:
    * **METHOD**: GET
    * **URL**: `{{base_url}}/tool`
    * **Header**: `Content-Type: application/json`
    * **Return Body**:

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

4. After locating the tool to delete, create a new request with the following values:
    * **METHOD**: DELETE
    * **URL**: `{{base_url}}/tool/{toolTitle}`
    * **Header**: `Content-Type: application/json`
    * **Request Body**: `{}`
5. To confirm the tool is no longer in the "toolbox," create a request with the following values:
    * **METHOD**: GET
    * **URL**: `{{base_url}}/tool/{previoustoolTitle}`
    * **Header**: `Content-Type: application/json`
    * **Request Body**: `{}`
6. Postman returns the following response if the deletion was successful: `{}` along with a "404 Not Found" error.

## Result

You can now locate and delete old tools by name in HaciendaOps.
