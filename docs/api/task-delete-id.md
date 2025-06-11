# Delete task (ID)

Removes a [`task`](task.md) object specified by the `id` parameter.

## Request URL

**Method**: `DELETE`

**URL**: `{{base_url}}/task/{taskId}`

## Parameter

| Name | Variable |
| ---- | ---------|
| base_url | string |
| task | string |
| taskId | integer |

## Header

**Content-Type:** `application/json`

## Request body

N/A

## Return body

`
{}
`

## Responses

* 200: Successful
* 404: Task object not found
* ECONNREFUSED: HaciendaOps is offline
