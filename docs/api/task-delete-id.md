# Delete task by ID

Removes a [`task`](task.md) object specified by the `id` parameter.

## Request URL

**Method**: `DELETE`

**URL**: `{{base_url}}/task/{taskId}`

## Properties

| Property name | Variable |
| ---- | ---------|
| `taskId` | integer |

## Header

**Content-Type:** `application/json`

## Request body

N/A

## Response body

`{}`

## Responses

* 200: Successful
* 404: Task object not found
* ECONNREFUSED: HaciendaOps is offline
