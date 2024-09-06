import requests

def get_attachment_by_id(attachment_id):
    # Your code here
    titles = " "

    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    response_body = response.json()

    for post in response_body["posts"]:
        for attachment in post["attachments"]:
            if attachment_id == attachment["id"]:

                return attachment["title"]

print(get_attachment_by_id(137))