import requests

url = "http://ecolens.cn"
data = {"key": "value"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)

print(response.text)
