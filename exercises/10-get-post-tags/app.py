import requests

def get_post_tags(post_id):
    # Your code here
    tags = []

    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    response_body = response.json()

    for post in response_body["posts"]:
        if post_id == post["id"]:
            tags = post["tags"]

    return tags


print(get_post_tags(146))