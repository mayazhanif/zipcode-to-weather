import requests
import json
import pandas as pd
df = pd.DataFrame()
zipcodeapikey="" #API KEY FROM https://www.zipcodeapi.com/API
openweathermapapi="" #API KEY FROM https://www.openweathermap.org/
response = requests.get('https://www.zipcodeapi.com/rest/'+zipcodeapikey+'/city-zips.json/San Francisco/CA') 
if response.status_code == 200:
    zipcodelist = json.loads(response.text)
    zipcodelist=zipcodelist["zip_codes"]
for zipcode in zipcodelist:
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+'&appid='+zipcodeapikey+'')
    if response.status_code == 200:
        weatherreponse=json.loads(response.text)
        df2 = pd.DataFrame([[weatherreponse["weather"][0]["description"], weatherreponse["main"]["temp"], weatherreponse["main"]["feels_like"], weatherreponse["main"]["pressure"], weatherreponse["main"]["humidity"]]])
        df=df.append(df2, ignore_index=True)
print(df)
