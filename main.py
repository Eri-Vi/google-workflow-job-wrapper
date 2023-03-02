import base64
import json
import random
import requests
import google.auth.transport.requests

credentials, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
auth_req = google.auth.transport.requests.Request()

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
    credentials.refresh(auth_req)
    token = credentials.token

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
