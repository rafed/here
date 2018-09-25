import requests
import json
from datetime import datetime, timedelta
import mysql.connector

appID = "LqJ21lDTyLEeGYbu4t6K"
appCode = "JaJrcnY2K-ocT9MxyhzHqA"

mydb = mysql.connector.connect(
  host="localhost",
  user="here",
  passwd="here",
  database="here"
)
mycursor = mydb.cursor()

coordinates = [
    ((28.747193,77.091064),(28.663211,77.1978375)),
    ((28.663211,77.091064),(28.579229,77.1978375)),
    ((28.579229,77.091064),(28.495247,77.1978375)),
    ((28.747193,77.1978375),(28.663211,77.304611)),
    ((28.663211,77.1978375),(28.579229,77.304611)),
    ((28.579229,77.1978375),(28.495247,77.304611))
    ## ((28.614439,77.144623),(28.665286,77.260580)) ## previous coord for test
]

dt = datetime.now() - timedelta(minutes=30)
date = dt.strftime("%d-%m-%Y")
time = dt.strftime("%H:%M")
weekday = dt.today().weekday()

rows = []

for pointX,pointY in coordinates:
    lat1,long1=pointX
    lat2,long2=pointY

    latmid = (lat1+lat2)/2
    longmid = (long1+long2)/2

    weatherURL = "https://weather.api.here.com/weather/1.0/report.json?app_id=%s&app_code=%s&product=observation&oneobservation=true&latitude=%s&longitude=%s" % (appID, appCode, latmid, longmid)
    trafficURL = "https://traffic.api.here.com/traffic/6.2/flow.json?app_id=%s&app_code=%s&bbox=%s,%s;%s,%s&responseattributes=sh" % (appID, appCode, lat1, long1, lat2, long2)

    r = requests.get(weatherURL)
    weather_data = r.text
    if r.status_code != 200:
        print "Weather request error"
        with open("error.log.txt", "a") as error:
            s = "[%s] Weather request error: %s %s\n" % (datetime.now(), r.status_code, weather_data)
            error.write(s)

    try:
        weather_json = json.loads(r.text)
    except Exception as e:
        print "Weather JSON parse error"
        with open("error.log.txt", "a") as error:
            s = "[%s] %s\n" % (datetime.now(), e)
            error.write(s)

    try:
        observations = weather_json['observations']
        location = observations['location'][0]
        observation = location['observation'][0]

        daylight = observation['daylight']
        temperature = observation['temperature']
        humidity = observation['humidity']
        windspeed = observation['windSpeed']
        rainDesc = observation['precipitationDesc']
        rainfall = observation['rainFall'] if 'rainFall' in observation else ""
    except Exception as e:
        print "Weather data accessing error"
        with open("error.log.txt", "a") as error:
            s = "[%s] %s\n" % (datetime.now(), e)
            error.write(s)
        fname = str(datetime.now()) + ".weather.txt"
        with open(fname, "w") as jsonFile:
            jsonFile.write(weather_data)

    r = requests.get(trafficURL)

    if r.status_code != 200:
        print "Traffic request error"
        with open("error.log.txt", "a") as error:
            s = "[%s] Traffic request error: %s %s\n" % (datetime.now(), r.status_code, r.text)
            error.write(s)
        exit(1)

    try:
        traffic_json = json.loads(r.text)
    except Exception as e:
        print "JSON parse error"
        with open("error.log.txt", "a") as error:
            s = "[%s] %s\n" % (datetime.now(), e)
            error.write(s)
        fname = str(datetime.now()) + ".traffic.txt"
        with open(fname, "w") as jsonFile:
            jsonFile.write(r.text)
        exit(1)

    try:
        for RWS in traffic_json['RWS']:
            for RW in RWS['RW']:
                for FIS in RW['FIS']:
                    LI = RW['LI']
                    if LI[4] == "-":
                        src = RW['DE']
                        for FI in FIS['FI']:
                            dst = FI['TMC']['DE']
                            LE = FI['TMC']['LE']
                            CN = FI['CF']['CN']
                            SP = FI['CF'][0]['SP']
                            SU = FI['CF'][0]['SU']
                            FF = FI['CF'][0]['FF']
                            JF = FI['CF'][0]['JF']
                            SHP = FI['SHP'][0]['value'][0]
                    else:
                        dst = RW['DE']
                        for FI in FIS['FI']:
                            src = FI['TMC']['DE']
                            LE = FI['TMC']['LE']
                            CN = FI['CF'][0]['CN']
                            SP = FI['CF'][0]['SP']
                            SU = FI['CF'][0]['SU']
                            FF = FI['CF'][0]['FF']
                            JF = FI['CF'][0]['JF']
                            SHP = FI['SHP'][0]['value'][0]
                    
                    row =   (src, dst, LE, CN, SP, SU, FF, JF, SHP, \
                            weekday, temperature, daylight, humidity, \
                            rainfall, rainDesc, windspeed, date, time, 0) # 0 for not holiday
                    rows.append(row)
    except Exception as e:
        print "Field access error in traffic json!"
        with open("error.log.txt", "a") as error:
            s = "[%s] %s\n" % (datetime.now(), e)
            error.write(s)
        
        fname = str(datetime.now()) + ".traffic.txt"
        with open(fname, "w") as jsonFile:
            jsonFile.write(r.text)

        fname = str(datetime.now()) + ".weather.txt"
        with open(fname, "w") as jsonFile:
            jsonFile.write(r.text)    
        exit(1)

    try:
        query = "insert into data values (%s" + ",%s"*18 + ")" ## %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        mycursor.executemany(query, rows)
        mydb.commit()
    except Exception as e:
        print "Database error"
        with open("error.log.txt", "a") as error:
            s = "[%s] %s\n" % (datetime.now(), e)
            error.write(s)

        fname = str(datetime.now()) + ".traffic.txt"
        with open(fname, "w") as jsonFile:
            jsonFile.write(r.text)

        fname = str(datetime.now()) + ".weather.txt"
        with open(fname, "w") as jsonFile:
            jsonFile.write(r.text)    
        exit(1)