# Get tools

Obtains a list of available [`tool`](tool.md) objects from the HaciendaOps instance.

## Request URL

**Method**: `GET`

**URL**: `{{base_url}}/tool`

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
]
```

## Responses

* 200: Successful
* 404: Task object not found
* ECONNREFUSED: HaciendaOps is offline
