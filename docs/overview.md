# HaciendaOps field guide (HFG)

The HaciendaOps field guide is a lightweight resource for field workers and new hires. It contains trusted information about plant species, animal traits, and tool usage. By using an API inspired by a traditional to-do list, small farms can simplify their agricultural responsibilities with task automation.

## What is the HaciendaOps field guide?

This REST API is a tool that allows small farms and agricultural teams to track ongoing tasks and support both fieldwork and trading activities.

Farmers can also record produce-to-market steps and retrieve their daily priorities or task updates with ease. By combining
the task management features of the API along with the record keeping features of monitoring animal species on the farm,
the entire ecosystem can be adequately tracked.

## Why it matters

- Improves field safety
- Reduces mistakes (e.g., using toxic plants or wrong tools)
- Supports e-learning and visual training

## Integration

Each entry includes a `kaizen_notes` section for observations or improvements from the field, which may be reviewed and approved over time.

## Features

- Assign and record ongoing tasks
- Monitor animals
    - Update last seen timestamp

## HaciendaOps prerequisites

- A [GitHub account](https://github.com)
- A development system running a current version or a
long-term support, also known as `LTS`, version of the Windows, MacOS, or Linux operating system.
- The following software on your development system:
    - [Git, command line](https://docs.github.com/en/get-started/quickstart/set-up-git)
    - Optionally, [GitHub Desktop](https://desktop.github.com).
    - A fork of the [HaciendaOps repository](https://github.com/rgmejiagroup/HaciendaOps)
    - A current or `LTS` version of `node.js`
    - Version 0.17.4 or later of [json-server](https://www.npmjs.com/package/json-server)
    - A current copy of the database file. You can get this by syncing your fork.

## Contributing to the API

You can submit a pull request for review to update the existing API documentation for the resources in HaciendaOps.
This can include bug fixes, code changes, proposing a new addition, or just maintaining out-of-date resources.
To contribute, follow the steps below:

1. Fork this repository to your GitHub account.
2. Confirm you can build a local copy of the documentation from your fork.
3. Install [Vale](https://vale.sh/) on your development or editing computer.
   To help you have a successful pull request experience, it's also helpful
   to add these extensions if you edit with the following assistants:
    - Markdownlint
    - Vale
4. A successful pull request:
    - Must not require more content in order for your pull request to work
    - Must help the end user of the product
    - Must have no lint or Vale errors
    - Must have no errors in any code examples
5. Test your changes locally from your feature branch before submission.

