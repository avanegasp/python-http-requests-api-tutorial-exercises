import requests

# Your code here

response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

response_body = response.json()

print(response_body)