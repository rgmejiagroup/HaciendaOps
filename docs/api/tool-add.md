# Add tool

Adds a [`tool`](tool.md) object to the HaciendaOps instance.

## Request URL

**Method**: `POST`

**URL**: `{{base_url}}/tool/{toolId}`

## Properties

| Property name | Type | Description |
| ------------- | ----------- | ----------- |
| `id` | integer | The tool's unique record ID |
| `name` | string | The name of the tool |
| `usage` | string | The tool's intended purpose |
| `safety_notes` | string | Saftey information for the tool |
| `training_required` | boolean | If false, no training necessary to use the tool. If true, training is required to use the tool. |
| `kaizen_notes` | string | Details about tool improvements |

## Header

**Content-Type:** `application/json`

## Request body

```json

[
    {
        "id": "1",
        "name": "Machete",
        "usage": "Clearing light brush manually",
        "safety_notes": "Always sheath after use",
        "training_required": false,
        "kaizen_notes": "Preferred over sickle for zone clearing by Rosa"
    }
]
```

## Response body

```json

[
    {
        "id": "1",
        "name": "Machete",
        "usage": "Clearing light brush manually",
        "safety_notes": "Always sheath after use",
        "training_required": false,
        "kaizen_notes": "Preferred over sickle for zone clearing by Rosa"
    }
]
```

## Responses

* 200: Successful
* 404: Task object not found
* ECONNREFUSED: HaciendaOps is offline
