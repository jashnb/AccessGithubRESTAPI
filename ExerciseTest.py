import json
import requests

my_token = "mypublictoken"
my_username = "jashnb"

r = requests.get('https://api.github.com/users/' + my_username + '/repos', headers={'Authorization': 'token ' + my_token})

jsonResponse = json.loads(r.text)

for item in jsonResponse:
    print(item['name'])