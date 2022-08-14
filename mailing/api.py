import json, os, requests

def send_message(message_id: int, phone: int, text: str):
    server_url = f'https://probe.fbrq.cloud/v1/send/{message_id}'
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {os.getenv("fabiqueVtoken")}',
        'Content-Type': 'application/json'
    }
    values = {
        "id": message_id,
        "phone": phone,
        "text": text
    }
    return requests.post(url=server_url, data=json.dumps(values), headers=headers).status_code

print(send_message(2, 79630470169, "цвавыаываыва"))