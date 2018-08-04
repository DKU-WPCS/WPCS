import urllib.request
from urllib.parse import urlencode, quote_plus
import urllib.parse
import json
import os

'''
2 : REH = 습도 (% 단위)
3 : RN1 = 1시간 강수량 (mm 단위)
5 : T1H = 기온 (섭씨)
7 : VEC = 풍향 
9 : WSD = 풍속

pm10 pm25 REH RN1 T1H VEC WSD 가 1개의 feature

'''

air_url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
weather_url = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib'

air_service_key = 'v2cJAMB3TyzncFsrAY5OYI9SyVn9d2560krPsgNXhFB%2F6fh15KNa0ayQQVZuyusYvk0RDXVYowK4j9z7Rk%2FRGw%3D%3D'
weather_service_key = 'v2cJAMB3TyzncFsrAY5OYI9SyVn9d2560krPsgNXhFB%2F6fh15KNa0ayQQVZuyusYvk0RDXVYowK4j9z7Rk%2FRGw%3D%3D'

x_axis = 60
y_axis = 127

air_key = {
quote_plus('numOfRows'): '20',
quote_plus('pageNo'): '1',
quote_plus('stationName'):'종로구',
quote_plus('dataTerm'): 'DAILY',
quote_plus('ver'): '1.3'
}

weather_key = {
quote_plus('base_date'):'',
quote_plus('base_time'):'',
quote_plus('nx'):x_axis,
quote_plus('ny'):y_axis,
quote_plus('numOfRows'):'20',
quote_plus('pageNo'):'1',
quote_plus('_type'):'json'
}

air_QueryParam = '?' + 'serviceKey=' + air_service_key + '&' +urlencode(air_key) + '&_returnType=json'

air_json = urllib.request.urlopen(air_url+air_QueryParam).read()
print(air_json)
with open('air_data.json','wb') as f:
    f.write(air_json)

class pm10Error(Exception):
    def __str__(self):
        return "PM10 HAS AN UNEXPECTED VALUE ... PASS"

class pm25Errror(Exception):
    def __str__(self):
        return  "PM25 HAS AN UNEXPECTED VALUE ... PASS"

class REHError(Exception):
    def __str__(self):
        return "REH HAS AN UNEXPECTED VALUE ... PASS"

class RN1Error():
    def __str__(self):
        return "RN1 HAS AN UNEXPECTED VALUE ... PASS"

class T1HError():
    def __str__(self):
        return "T1H HAS AN UNEXPECTED VALUE ... PASS"

class VECError():
    def __str__(self):
        return "VEC HAS AN UNEXPECTED VALUE ... PASS"

class WSDError():
    def __str__(self):
        return "WSD HAS AN UNEXPECTED VALUE ... PASS"

def Pm10ToInt(pm10_value):

    try:
        return int(pm10_value)
    except ValueError:
        raise pm10Error

def Pm25ToInt(pm25_value):

    try:
        return int(pm25_value)
    except ValueError:
        raise pm25Errror

def REHToInt(REH_value):

    try:
        return int(REH_value)
    except:
        raise REHError

def RN1ToInt(RN1_value):

    try:
        return int(RN1_value)
    except:
        raise RN1Error

def T1HToInt(T1h_value):

    try:
        return int(T1h_value)
    except:
        raise T1HError

def VECToInt(VEC_value):

    try:
        return int(VEC_value)
    except:
        raise VECError

def WSDToInt(WSD_value):

    try:
        return int(WSD_value)
    except:
        raise WSDError

with open('air_data.json', 'rt', encoding='UTF-8') as air:

    air_data = json.load(air)

    feature = []

    for i in range(len(air_data['list'])):

        String = [x for x in air_data['list'][i]['dataTime'].split()]

        base_date = String[0].replace('-', '')
        base_time = String[1].replace(':', '')

        weather_key[quote_plus('base_date')] = base_date
        weather_key[quote_plus('base_time')] = base_time

        weather_QueryParam = '?' + 'serviceKey=' + weather_service_key + '&' + urlencode(weather_key)
        print(weather_QueryParam)
        weather_json = urllib.request.urlopen(weather_url + weather_QueryParam).read()
        print(weather_json)
        with open('weather_data.json', 'wb') as weather:
            weather.write(weather_json)

        with open('weather_data.json', 'rt', encoding='UTF-8') as weather:
            weather_data = json.load(weather)

        try:
            col = []
            pm10 = Pm10ToInt(air_data['list'][i]['pm10Value'])
            pm25 = Pm25ToInt(air_data['list'][i]['pm25Value'])

            REH = REHToInt(weather_data['response']['body']['items']['item'][2]['obsrValue'])
            RN1 = RN1ToInt(weather_data['response']['body']['items']['item'][3]['obsrValue'])
            T1H = T1HToInt(weather_data['response']['body']['items']['item'][5]['obsrValue'])
            VEC = VECToInt(weather_data['response']['body']['items']['item'][7]['obsrValue'])
            WSD = WSDToInt(weather_data['response']['body']['items']['item'][9]['obsrValue'])

            col.append(pm10)
            col.append(pm25)
            col.append(REH)
            col.append(RN1)
            col.append(T1H)
            col.append(VEC)
            col.append(WSD)

            feature.append(col)
        except pm10Error as e:
            col = []
            print(e)
        except pm25Errror as e:
            col = []
            print(e)
        except REHError as e:
            col = []
            print(e)
        except RN1Error as e:
            col = []
            print(e)
        except T1HError as e:
            col = []
            print(e)
        except VECError as e:
            col = []
            print(e)
        except WSDError as e:
            print(e)

if os.path.isfile("dataset.txt"):
    with open("dataset.txt", 'a') as f:
        for row in feature:
            for col in row:
                f.write(str(col) + ' ')
            f.write("\n")
else:
    with open("dataset.txt", 'w') as f:
        for row in feature:
            for col in row:
                f.write(str(col) + ' ')
            f.write("\n")