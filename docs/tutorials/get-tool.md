# View list of tools

The HaciendaOps API allows users to view the existing "toolbox" of all tools available on the farm.

## Prerequisites

* An existing database with tools
* Access to a command line or Postman
    * This tutorial uses Postman, but can use the command line to make the necessary REST API calls. If using the command line, cURL is necessary to complete
      any API requests.

## Checking the toolbox

1. Start running a local HaciendaOps instance.
   * To start the instance, run the following command:

     ```shell
     cd /HaciendaOps/api
     json-server -w hfg-db.json
     ```

2. Open the Postman app on your computer.

3. Create a new request with the following values:
    * **METHOD**: GET
    * **URL**: `{{base_url}}/tool`
    * **Header**: `Content-Type: application/json`

## Result

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
    
You can now locate the full list of available tools in the HaciendaOps "toolbox."
