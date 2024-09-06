import requests

def get_titles():
    titles = []
    # Your code here

    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    response_body = response.json()

    # print(response_body)

    for index, post in enumerate(response_body["posts"]):
        titles.append(post["title"])

    return titles


print(get_titles())