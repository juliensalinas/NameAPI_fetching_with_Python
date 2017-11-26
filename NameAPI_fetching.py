"""
Fetch the NameAPI.org REST API and turn JSON response into Python dict.

Sent data have to be JSON data encoded into request body.
Send request headers must be set to 'application/json'.
"""

import requests

# url of the NameAPI.org endpoint:
url = (
    "http://rc50-api.nameapi.org/rest/v5.0/parser/personnameparser?"
    "apiKey=<API-KEY>"
)

# Dict of data to be sent to NameAPI.org:
payload = {
    "inputPerson": {
        "type": "NaturalInputPerson",
        "personName": {
            "nameFields": [
                {
                    "string": "Petra",
                    "fieldType": "GIVENNAME"
                }, {
                    "string": "Meyer",
                    "fieldType": "SURNAME"
                }
            ]
        },
        "gender": "UNKNOWN"
    }
}

# Proceed, only if no error:
try:
    # Send request to NameAPI.org by doing the following:
    # - make a POST HTTP request
    # - encode the Python payload dict to JSON
    # - pass the JSON to request body
    # - set header's 'Content-Type' to 'application/json' instead of
    #   default 'multipart/form-data'
    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    # Decode JSON response into a Python dict:
    resp_dict = resp.json()
    print(resp_dict)
except requests.exceptions.HTTPError as e:
    print("Bad HTTP status code:", e)
except requests.exceptions.RequestException as e:
    print("Network error:", e)
