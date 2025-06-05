# Update tool (safety_notes)

Updates a [`tool`](tool.md) object's saftey information in the HaciendaOps instance.

## Request URL

**Method**: `PATCH`

**URL**: `{{base_url}}/tool/1`

## Parameter

| Property name | Type | Description |
| ------------- | ----------- | ----------- |
| `id` | number | The task's unique record ID |
| `name` | string | The name of the tool |
| `usage` | string | The tool's intended purpose |
| `safety_notes` | string | Saftey information for the tool |
| `training_required` | boolean | If false, no training necessary to use the tool |
| `kaizen_notes` | string | Details about task improvements |

## Header

**Content-Type:** `application/json`

## Request body

```json

{
    "safety_notes": "Always sheath after use and return to drawer",
}
```

## Return body

```json

{
    "id": "1",
    "name": "Machete",
    "usage": "Clearing light brush manually",
    "safety_notes": "Always sheath after use and return to drawer",
    "training_required": false,
    "kaizen_notes": "Preferred over sickle for zone clearing by Rosa"
}
```

## Responses

* 200: Successful
* 404: Task object not found
* ECONNREFUSED: HaciendaOps is offline
