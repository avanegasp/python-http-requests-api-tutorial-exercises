import requests

# Your code here
response = requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")

response_body = response.json()

print(response_body["name"])