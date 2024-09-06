import requests

# Your code here

response = requests.post("https://assets.breatheco.de/apis/fake/sample/post.php")

response_body = response.text

print(response_body)

