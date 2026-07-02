import json
import requests

from config import GEMINI_API_KEY, GEMINI_MODEL


URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"


def generate_response(messages, assessments):

    context = ""

    for assessment in assessments:

        context += f"""
Assessment:
{assessment['name']}

URL:
{assessment['url']}

Description:
{assessment['document']}
"""

    conversation = ""

    for message in messages:

        conversation += f"{message['role']}: {message['content']}\n"

    prompt = f"""
You are SHL's Assessment Recommendation Assistant.

Use ONLY the retrieved assessments provided below.

Do not invent new assessments.
Do not invent URLs.

In your reply:
- Briefly explain why these assessments fit the user's needs.
- Mention only assessments present in the retrieved list.
- Do not output JSON.
- Keep the response concise (100–150 words).

Conversation:

{conversation}

Retrieved Assessments:

{context}

Recommend the most suitable assessments with short explanations.
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.2
        }
    }

    response = requests.post(
        URL,
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    response.raise_for_status()

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]