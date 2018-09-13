import requests
import json

appID = "LqJ21lDTyLEeGYbu4t6K"
appCode = "JaJrcnY2K-ocT9MxyhzHqA"

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
            "&responseattributes=sh,fc"
            )

#           "&bbox=28.469295,76.967812;28.672817,77.431641"

r = requests.get(location)
# r = requests.get(weather)

print r.status_code

result = json.loads(r.text)
print json.dumps(result, indent=2, sort_keys=True)