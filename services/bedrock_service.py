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

Return ONLY one JSON object.

Do not include:
- explanations
- markdown
- code fences
- comments
- extra text

Your entire response must be a single JSON object.

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

# Remove markdown
    if ai_response.startswith("```"):
        ai_response = ai_response.replace("```json", "")
        ai_response = ai_response.replace("```", "")
        ai_response = ai_response.strip()

    print("AI RESPONSE:")
    print(ai_response)

# Keep only the first JSON object
    start = ai_response.find("{")
    end = ai_response.rfind("}") + 1

    json_text = ai_response[start:end]

    print("JSON ONLY:")
    print(json_text)

    return json.loads(json_text)