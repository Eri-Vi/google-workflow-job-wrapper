import random
import time
import urllib

import google.auth.transport.requests
import google.oauth2.id_token


def run_job(event, context):
  data = base64.b64decode(event['data']).decode('utf-8')
  print(data)

  auth_req = google.auth.transport.requests.Request()
  id_token = google.oauth2.id_token.fetch_id_token(auth_req, data['url'])

  req = urllib.request.Request(data['url'])
  req.add_header('Authorozation', f'Bearer {id_token}')

  state = random.randint(0,1)

  if state == 0:
    print('mock success')
    response = urllib.request.urlopen(req)
    return 'ok', 200
  else:
    print('mock timeout')
    return 'ok', 200
