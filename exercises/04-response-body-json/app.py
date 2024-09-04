import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")

response_body = response.json()
print("Current time:", response_body["hours"] + " hrs " + response_body["minutes"] + " min and " + response_body["seconds"] + " sec")