import requests
data = ['this', 'is', 'a', 'test']

resp = requests.post(url, data=data, auth=(usr, pwd))
