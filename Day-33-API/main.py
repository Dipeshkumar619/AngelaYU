# cfpo
# commands , functions,protocols,objects
# import requests
# response=requests.get(url="http://api.open-notify.org/iss-now.json")
# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")
# elif response.status_code == 404:
#     raise Exception("Requested Resource doesn't exist")
# elif response.status_code == 401:
#     raise Exception("Requested is Unauthorized")
# else:
#     data=response.json()
#     location=(data["iss_position"]["longitude"],data["iss_position"]["latitude"])
#     print(data)
#     print(location)


# import requests
# response=requests.get(url="https://api.kanye.rest/")
# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")
# elif response.status_code == 404:
#     raise Exception("Requested Resource doesn't exist")
# elif response.status_code == 401:
#     raise Exception("Requested is Unauthorized")
# else:
#     data=response.json()
#     print(data)

MY_LAT=28.704060
MY_LONG=77.102493
import requests
from datetime import datetime
parameters={
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response=requests.get(url="http://api.sunrise-sunset.org/json",params=parameters)
data=response.json()
sunrise=data["results"]["sunrise"]
sunset=data["results"]["sunset"]
print(sunrise,sunset)
timenow=datetime.now()
print(timenow.hour)
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])
