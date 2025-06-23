---
layout: page
---

# `task` resource

## Base endpoint

```shell

{base_url}/task
```

Provides information about pending and ongoing tasks at the farm using HaciendaOps API.

## Resource properties

Sample `task` resource

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

| Property name | Type | Description |
| ------------- | ----------- | ----------- |
| `id` | integer | The task's unique record ID |
| `title` | string | The title of the task |
| `description` | string | A short description of the task |
| `task_type` | string | The task's category |
| `due_date` | string | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format of the date and time the task is due |
| `completed` | string | The status of the task |
| `kaizen_notes` | string | Details about task improvements |

## Read

* [Get all tasks](./task-get-all.md)

## Create

* [Add a new task](./task-add.md)

## Update

* [Patch a task's completion status](./task-update-completed.md)
* [Put an entire task](./task-update-all.md)

## Delete

* [Delete a task by ID](./task-delete-id.md)
