# GET POST PUT DELETE
import requests
from datetime import datetime
import html
USERNAME="nirala"
token="028f80163238f7e8749580d183d65fc6"
GRAPH_ID="graph1"
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
pixela_endpoint="https://pixe.la/v1/users"
graph_endpoint=f"https://pixe.la/v1/users/{USERNAME}/graphs"
add_pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230524"

params={
    "token": "028f80163238f7e8749580d183d65fc6",
        "username": "nirala",
        "agreeTermsOfService": "yes",
        "notMinor": "yes",

}
# response=requests.post(url=pixela_endpoint,json=params,verify=False)
# print(response.json())
today=datetime.now()
params1={
    "id": "graph1",
    "name": "workout",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}
params2={
    "quantity": "10",
}
headers={
    "X-USER-TOKEN": token
}
response=requests.delete(url=update_pixel_endpoint,headers=headers,verify=False)
print(response.text)
# print(response.json())