import requests
import html
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
LAT=28.704060
LON=77.102493
API_KEY=""
weather_params={
    "lat":LAT,
    "lon":LON,
    "appid":API_KEY,
}
OWM_Endpoint="https://api.openweathermap.org/data/2.5/weather"
response=requests.get(OWM_Endpoint,params=weather_params,verify=False)
data=response.json()
print(data)

# Download the helper library from https://www.twilio.com/docs/python/install
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+12542684672",
  to="+"
)
print(message.sid)