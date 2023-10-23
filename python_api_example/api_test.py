import requests

# GET
url_endpoint = 'http://127.0.0.1:5000/uppercase'

response = requests.get(
    url= url_endpoint,
    params={'text': '7 70 seventy'})

print(response.json())