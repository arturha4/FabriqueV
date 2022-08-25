import json

import requests
from FabriqueVTestCase.wsgi import *


def send_message(message_id: int, phone: int, text: str):
    server_url = f'https://probe.fbrq.cloud/v1/send/{message_id}'
    fabrique_v_token = os.getenv('fabriqVtoken')
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {fabrique_v_token}',
        'Content-Type': 'application/json'
    }
    values = {
        "id": message_id,
        "phone": phone,
        "text": text
    }
    return requests.post(url=server_url, data=json.dumps(values), headers=headers).status_code
