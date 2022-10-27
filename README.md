# Running the service
The server used to run the WW1 events service exists in the server.py file. In this file, the server is started with the following code block:
```python
if __name__ == "__main__":
  app.run(host="127.0.0.1", port=5000, debug=True)
```
To execute this and start the server via command line, simply run: python3 server.py

Additionally, the server is preset to run locally on port 5000. To change the server host value, simply change the host value in server.py to your 
desired host (it is currently set to "127.0.0.1"). To change the server port value simply change the port value in server.py to your desired port 
(it is currently set to 5000).

# Requesting and Receiving Data
The API specification below details all aspects of the WW1 events service including:
* Media types allowed in the request body
* Media types provided by the server
* Request body attributes and types
* Response body attributes and types
* Example requests
* Example responses

## Requesting Data
Note: Please refer to the API spec below for additional details

Requests for WW1 events are to be sent as an HTTP GET request to the GET /events endpoint detailed in the API spec. If the server is running locally on
port 5000, the HTTP GET request would be sent to http://localhost:5000/events.

The request for WW1 events must include a request body containing a JSON object specifying the day and month to get WW1 events for. The day and month
attributes both must have integer values. An example request object is:

```
{
  "day": 10,
  "month": 5
}
```

## Receiving Data
Note: Please refer to the API spec below for additional details

Receiving data from the WW1 events service is done by capturing the JSON object returned in the response body of a successful request. The events data
sent back in response to a successful HTTP GET request will be in the response body and will be a JSON object containing an events array. The array will
contain JSON objects representing each event that took place on the day and month provided in the request. An example response object is:

```
{
    “events”: [
        {
            “event”: “Battle of Krivolak, first of the Salonika front”,
            “theater_front_campaign”: “Balkan, Macedonian”,
            “year”: 1915
        },
        {
            “event”: “Third Battle of the Isonzo
            “theater_front_campaign”: “Italian”,
            “year”: 1915
        },
        {
            “event”: “Conquest of Romania by Central Powers”,
            “theater_front_campaign”: “Balkan”,
            “year”: 1916
        },
    ]
}
```

## Example Requests
Programmatic example call with JavaScript:
```javascript
const callEventsService = async (month, day) => {
    try {
        // create HTTP request to GET /events endpoint and send request
        const response = await fetch({
            url: 'http://localhost:5000/events',
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            data: JSON.stringify({ month, day })
        });

        // request was successful
        if (response.status === 200) {
            // get events from response body
            const events = await response.json();
            // -- use events as data to be displayed in frontend UI --
        }
    } catch (err) {
        console.error(err);
    }
}
```

Example call with Postman:
![image](https://user-images.githubusercontent.com/76921481/198409114-c9acdd7d-7609-4566-b087-fc04b26afb3d.png)

## API Specification
<img width="689" alt="image" src="https://user-images.githubusercontent.com/76921481/198404680-910dbae5-b98f-477b-b74c-8a91ee344658.png">
<img width="689" alt="image" src="https://user-images.githubusercontent.com/76921481/198404952-a02e6454-4aac-4829-adec-faf69827c24c.png">
<img width="688" alt="image" src="https://user-images.githubusercontent.com/76921481/198405141-9475ebb1-8d17-4c1c-8e80-fe859b94d07a.png">
