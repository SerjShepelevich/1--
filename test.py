import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
data = json.loads(response.text)
print(data.items())

print(data.get('Valute').keys())
for i in data.get('Valute').keys():
    print(data.get('Valute').get(i))