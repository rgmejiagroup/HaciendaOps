---
layout: page
---

# HaciendaOps quickstart guide

After reading the [overview](./index.md) topic, you can review the existing API reference materials and learn how certain operations
work with the tutorials found in the documentation for this API.

## Tutorials

Before reviewing the tutorials, confirm you've completed and set up your development system with the [overview](./index.md) topic.

After confirming your development system is ready to begin operating the API, the following topics highlight the most commonly used tasks in HaciendaOps:

* Task management
    * [Adding a task](./tutorials/add-task.md)
    * [Deleting old tasks](./tutorials/delete-task-by-id.md)
    * [Updating in-progress tasks](./tutorials/update-task.md)

* Toolbox management
    * [Search the toolbox](./tutorials/get-tool.md)
    * [Removing broken tools](./tutorials/delete-tool-by-name.md)
    * [Updating saftey information for tools](./tutorials/update-tool.md)

## API reference docs

These topics offer in-depth descriptions of the resources available to configure while workers are in the field.

The API reference docs mention a `{base_url}` when referring to the URL of a resource. The `{base_url}` value depends
on the installation of the service, but when the API is running locally for testing, the `{base_url}` is commonly `http://localhost:3000`.

* [task resource](./api/task.md)
* [tool resource](./api/tool.md)
