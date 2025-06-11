# Code examples (tool)

**Author:** Lyle Zucker

## cURL example

Lists all tools, including name, intended purpose, saftey information, training requirements, and notes from workers.

### cURL command

```shell
curl http://localhost:3000/task
```

### cURL response

```shell
    {
        "id": "1",
        "name": "Machete",
        "usage": "Clearing light brush manually",
        "safety_notes": "Always sheath after use",
        "training_required": false,
        "kaizen_notes": "Preferred over sickle for zone clearing by Rosa"
      },
      {
        "id": "2",
        "name": "RFID Ear Tag Scanner",
        "usage": "Identify and track goats in fenced areas",
        "safety_notes": "Keep away from water; charge weekly",
        "training_required": true,
        "kaizen_notes": "Alex suggested waterproof case for rainy season"
    }
```

## Postman example

Add a note to a tool, indicating a change in process moving forward on the farm.

### Request

**Method**: PATCH

```shell
http://localhost:3000/tool/2
```

### Request data

```shell
{
    "kaizen_notes": "Consider upgrading to new model for improved latency and quicker response times"
}
```

### Postman response

```shell
    {
        "id": "2",
        "name": "RFID Ear Tag Scanner",
        "usage": "Identify and track goats in fenced areas",
        "safety_notes": "Keep away from water; charge weekly",
        "training_required": true,
        "kaizen_notes": "Consider upgrading to new model for improved latency and quicker response times"
    }
```
