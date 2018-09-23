import requests
import json

appID = "LqJ21lDTyLEeGYbu4t6K"
appCode = "JaJrcnY2K-ocT9MxyhzHqA"

doc = (
    "http://traffic.api.here.com/traffic/6.0/xsd/flow.xsd"
    "?app_id=" + appID +
    "&app_code=" + appCode
)

weather =   (
    "https://weather.api.here.com/weather/1.0/report.json"
    "?app_id=" + appID +
    "&app_code=" + appCode +
    "&product=observation"
    "&name=Dhaka"
)   

location =  (
    "https://traffic.api.here.com/traffic/6.2/flow.json"
    "?app_id=" + appID + 
    "&app_code=" + appCode +
    "&bbox=28.624347,77.205863;28.637060,77.335174"
    # "&tables=ECC+CCD+Table"
    # "&responseattributes=sh,fc"
)

# "&bbox=28.469295,76.967812;28.672817,77.431641"

# r = requests.get(doc)
# r = requests.get(location)
r = requests.get(weather)

if r.status_code != 200:
    print r.status_code
    exit(1)

# print r.text

result = json.loads(r.text)
print json.dumps(result, indent=2) #, sort_keys=True)