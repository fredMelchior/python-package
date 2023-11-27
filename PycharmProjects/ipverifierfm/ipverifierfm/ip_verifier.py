import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

response = urlopen(url)

data = json.load(response)

ip = data['ip']
org = data['org']
city = data['city']
country = data['country']

print(f'\nExternal IP details: \n')
print(f'IP: {ip}\nCompany: {org}\nCity: {city}\nCountry: {country}')