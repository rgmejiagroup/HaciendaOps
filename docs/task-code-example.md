# Code examples (task)

## cURL example

Lists all tasks, including title, description, type, due date, completion status, and notes from workers.

### cURL command

```shell
curl http://localhost:3000/task
```

### cURL response

```shell
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

## Postman example

Mark the routine morning irrigation task as incomplete for the workers in the morning shift.

### Request

**Method**: PATCH

```shell
http://localhost:3000/task/1
```

### Request data

```shell
{
    "completed": false,
}
```

### Postman response

```shell
    {
        "id": 1,
        "title": "Morning irrigation",
        "description": "Water the plants in Garden A",
        "task_type": "Watering",
        "due_date": "2024-06-05",
        "completed": false,
        "kaizen_notes": "Consider shifting to sunrise-only watering to reduce evaporation."
    }
```
