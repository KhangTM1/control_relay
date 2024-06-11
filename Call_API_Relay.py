import time
import requests
from requests.auth import HTTPBasicAuth

def control_relay(ip, state, username, password):
    # Define the URL and parameters
    url = f'http://{ip}/api'
    params = {
        'id': 0,
        'state': state
    }

    # Make the GET request with basic authentication
    response = requests.get(url, params=params, auth=HTTPBasicAuth(username, password))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response
        try:
            data = response.json()  # Assuming the response is in JSON format
            return data
        except ValueError:
            return response.text  # If response is not JSON
    else:
        return {
            'error': response.status_code,
            'message': response.text
        }
