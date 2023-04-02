import os
import requests


def lambda_handler(event, context):
    url = os.getenv('SLACK_URL')
    issue = event["issue"]["html_url"]
    payload: str = f"{{'text':'Issue Created: {issue}'}}"

    r = requests.post(url, payload)

    return r.text
