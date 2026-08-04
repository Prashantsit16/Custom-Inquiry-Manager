import boto3
import json


client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)


def summarize_inquiry(message):

    prompt = f"""
You are an AI customer support assistant.

Analyze the following customer inquiry.

Return ONLY valid JSON.

Format:

{{
    "summary": "...",
    "category": "...",
    "priority": "Low/Medium/High",
    "department": "..."
}}

Customer Inquiry:

{message}
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
            "maxTokens": 300,
            "temperature": 0.2
        }
    }

    response = client.invoke_model(
        modelId="global.amazon.nova-2-lite-v1:0",
        body=json.dumps(body)
    )

    response_body = json.loads(response["body"].read())
    ai_response = response_body["output"]["message"]["content"][0]["text"].strip()

    # Remove markdown if present
    if ai_response.startswith("```"):
        ai_response = ai_response.replace("```json", "")
        ai_response = ai_response.replace("```", "")
        ai_response = ai_response.strip()

    return json.loads(ai_response)