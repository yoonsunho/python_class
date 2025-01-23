import requests

response = requests.get(url='https://random-data-api.com/api/v2/users').json()

print(response)