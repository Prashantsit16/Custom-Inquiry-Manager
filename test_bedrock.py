import boto3
import json

client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

prompt = """
Summarize the following customer inquiry in one sentence.

Customer Inquiry:
I cannot log into my account after changing my password yesterday.
"""

body = {
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": prompt
                }
            ]
        }
    ],
    "inferenceConfig": {
        "maxTokens": 200,
        "temperature": 0.2
    }
}

response = client.invoke_model(
    modelId="global.amazon.nova-2-lite-v1:0",
    body=json.dumps(body)
)

response_body = json.loads(response["body"].read())

summary = response_body["output"]["message"]["content"][0]["text"]

print(summary)