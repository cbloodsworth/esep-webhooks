import json

def lambda_handler(event, context):
    issue = event["issue"]["html_url"]
    payload: str = f"{{'text':'Issue Created: {issue}'}}"
    return {
            'statusCode': 200,
            'body': json.dumps(payload)
    }
