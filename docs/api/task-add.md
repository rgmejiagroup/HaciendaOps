# Add task

Adds a [`task`](task.md) object to the HaciendaOps instance.

## Request URL

**Method**: `POST`

**URL**: `{{base_url}}/task/{taskId}`

## Properties

| Property name | Type | Description |
| ------------- | ----------- | ----------- |
| `id` | integer | The task's unique record ID |
| `title` | string | The title of the task |
| `description` | string | A short description of the task |
| `task_type` | string | The task's category |
| `due_date` | string | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format of the date and time the task is due |
| `completed` | boolean | The status of the task |
| `kaizen_notes` | string | Details about task improvements |

## Header

**Content-Type:** `application/json`

## Request body

```json
[
    {
        "id": 1,
        "title": "Morning irrigation",
        "description": "Water the plants in Garden A",
        "task_type": "Watering",
        "due_date": "2024-06-05",
        "completed": false,
        "kaizen_notes": "Consider changing to sunrise-only watering and reduce evaporation."
    }
]
```

## Response body

```json
[
    {
        "id": 1,
        "title": "Morning irrigation",
        "description": "Water the plants in Garden A",
        "task_type": "Watering",
        "due_date": "2024-06-05",
        "completed": false,
        "kaizen_notes": "Consider changing to sunrise-only watering and reduce evaporation."
    }
]
```

## Responses

* 200: Successful
* 404: Task object not found
* ECONNREFUSED: HaciendaOps is offline
