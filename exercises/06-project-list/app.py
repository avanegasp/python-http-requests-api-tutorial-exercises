import requests

# Your code here

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")

response_body = response.json()

print(response_body[1]["name"])