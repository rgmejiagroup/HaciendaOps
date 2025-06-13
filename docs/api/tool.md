---
layout: page
---

# `tool` resource

Base endpoint:

```shell

{server_url}/task
```

Provides information about tools at the farm, including how to use the tool and saftey details via the HaciendaOps API.

## Resource properties

Sample `tool` resource

```json

{
    "id": "1",
    "name": "Machete",
    "usage": "Clearing light brush manually",
    "safety_notes": "Always sheath after use",
    "training_required": false,
    "kaizen_notes": "Preferred over sickle for zone clearing by Rosa"
}
```

| Property name | Type | Description |
| ------------- | ----------- | ----------- |
| `id` | number | The task's unique record ID |
| `name` | string | The name of the tool |
| `usage` | string | The tool's intended purpose |
| `safety_notes` | string | Saftey information for the tool |
| `training_required` | boolean | If false, no training necessary to use the tool |
| `kaizen_notes` | string | Details about task improvements |

## Read

* [Get all tools](./api/tool-get-all.md)

## Create

* [Add a new tool](./api/tool-add.md)

## Update

* [Patch a tools's safety information](./api/tool-update-safety-information.md)

## Delete

* [Delete a tool by ID](./api/ttool-delete-id.md)
