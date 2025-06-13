# Delete tool

Deletes a [`tool`](tool.md) object from the HaciendaOps instance.

## Request URL

**Method**: `DELETE`

**URL**: `{{base_url}}/tool/{toolId}`

## Parameter

| Name | Variable |
| ---- | ---------|
| `toolId` | integer |

## Header

**Content-Type:** `application/json`

## Request body

N/A

## Response body

`
{}
`

## Responses

* 200: Successful
* 404: Task object not found
* ECONNREFUSED: HaciendaOps is offline
