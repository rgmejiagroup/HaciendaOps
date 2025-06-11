# Updating tools

The HaciendaOps API allows users to update tools with the intent to keep training and saftey information relevant.

## Prerequisites

* An existing database with tasks
* Access to a command line or Postman
    * This tutorial uses Postman, but can use the command line to make the necessary REST API calls.

## Update an existing tool

1. Confirm the local HaciendaOps instance is running.
   * If the service isn't running, run the following command:

     ```shell
     cd <your-github-workspace>/HaciendaOps/api
     json-server -w hfg-db.json

2. Open the Postman app on your computer.
3. For a list of the tools currently available in the toolbox, create a new request with the following values:
    * **METHOD**: GET
    * **URL**: `{{base_url}}/tool`
    * **Header**: `Content-Type: application/json`
    * **Return Body**:

```json
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

4. Once a tool needs safety or training updates, create a new request with the following values:
    * **METHOD**: PATCH
    * **URL**: `{{base_url}}/tool/{toolId}`
    * **Header**: `Content-Type: application/json`
    * **Request Body**:

```json

{
    "training_required": true,
}
```

5. To confirm the tool now has the correct information, create a request with the following values:
    * **METHOD**: GET
    * **URL**: `{{base_url}}/tool/{previoustoolId}`
    * **Header**: `Content-Type: application/json`
    * **Return Body**:

```json

    {
        "id": "1",
        "name": "Machete",
        "usage": "Clearing light brush manually",
        "safety_notes": "Always sheath after use",
        "training_required": true,
        "kaizen_notes": "Preferred over sickle for zone clearing by Rosa"
    }
```

6. Postman returns the preceeding response if the tool modification was successful.

## Result

You can now update existing tools in HaciendaOps.
