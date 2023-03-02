import base64
import json
import random
import requests
from google.auth.transport.requests import Request
from google.oauth2 import id_token
from google.auth import default

# This function is triggered by a Pub/Sub message containing a JSON payload
def process_message(event, context):
  state = random.randint(0,1)

  if state == 0:
    print('Mock job success')
    # Decode the Base64-encoded message payload
    message_data = base64.b64decode(event['data']).decode('utf-8')
    message = json.loads(message_data)
    url = message['url']

    # Generate an ID token using the default service account's credentials
    request = Request()
    token = id_token.fetch_id_token(request, url)

    # Make the GET request to the specified URL using the generated ID token as the Authorization header
    headers = {
      'Authorization': f'Bearer {token}',
      'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)

    # Log the response
    print(f"GET request to {url} returned {response.status_code}: {response.text}")
  else:
    print('Mock job timeout')
