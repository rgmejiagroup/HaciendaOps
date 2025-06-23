# Get tasks

Obtains a list of [`task`](task.md) objects from the HaciendaOps instance.

## Request URL

**Method**: `GET`

**URL**: `{{base_url}}/task/`

## Properties

N/A

## Header

**Content-Type:** `application/json`

## Request body

N/A

## Return body

```json
[
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
]
```

## Responses

* 200: Successful
* 404: Task object not found
* ECONNREFUSED: HaciendaOps is offline
