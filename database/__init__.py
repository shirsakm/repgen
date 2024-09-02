import requests

with open('keys/api.key') as keyfile:
    API_KEY = keyfile.read().strip()

URL = "https://cloud.seatable.io/api/v2.1/dtable/app-access-token/"

headers = {
    "accept": "application/json",
    "authorization": f"Bearer {API_KEY}",
}

response = requests.get(URL, headers=headers)
base_uuid = response.json()['dtable_uuid']

URL = f"https://cloud.seatable.io/api-gateway/api/v2/dtables/{base_uuid}/sql"

payload = {
    "sql": "SELECT * FROM Table1",
    "convert_keys": True,
    "server_only": False
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(URL, json=payload, headers=headers)

print(response.text)