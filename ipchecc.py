import requests
import json

url = 'https://api.abuseipdb.com/api/v2/check'

ip = input("url/ip: ")

querystring = {
    'ipAddress': ip
}

headers = {
    'Accept': 'application/json',
    'Key': '6ca068a91b7a3ceb1b2fd358d5f0539fb6f6c01036bfdfa94b96c0b1ac6b7b61716ab017ea5d0216'
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
decodedResponse = json.loads(response.text)
print(json.dumps(decodedResponse, sort_keys=True, indent=4))