import requests
from datetime import datetime as d

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME =  "ionyejekwe"
TOKEN = "wriywr98438ewue239"
GRAPHID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
#
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}
today = d.now()
pixel_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_url = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

response = requests.post(url=pixel_url, json=pixel_body, headers=headers)
print(response.text)