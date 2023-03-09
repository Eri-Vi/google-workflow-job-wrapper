import base64
import json
import random
import requests
import google.auth.transport.requests

credentials, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
auth_req = google.auth.transport.requests.Request()

# This function is triggered by a Pub/Sub message containing a JSON payload
def process_message(event, context):
  # Decode the Base64-encoded message payload
  message_data = base64.b64decode(event['data']).decode('utf-8')
  message = json.loads(message_data)
  url = message['url']
  status = message['status']

  print(f'Mock job status: {status}')

  if status == 'timeout':
    return True
  else:
    # Generate an ID token using the default service account's credentials
    credentials.refresh(auth_req)
    token = credentials.token

    # Make the POST request to the specified URL using the generated ID token as the Authorization header
    headers = {
      'Authorization': f'Bearer {token}',
      'Content-Type': 'application/json'
    }

    data = {'status': status}
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Log the response
    print(f"POST request to {url} returned {response.status_code}: {response.text}")
    return True
