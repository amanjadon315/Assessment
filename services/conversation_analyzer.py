import json
import requests

from config import GEMINI_API_KEY, GEMINI_MODEL


URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"


SYSTEM_PROMPT = """
You are an information extraction engine.

Your ONLY job is to analyze the conversation and return JSON.

Do NOT answer the user.

Return ONLY valid JSON.

Schema:

{
  "intent": "recommend | compare | refine",
  "out_of_scope": false,
  "context": {
      "role": null,
      "job_level": null,
      "purpose": null,
      "skills": [],
      "language": null,
      "assessment_categories": [],
      "assessment_names": []
  }
}

Assessment categories must only use these values:

Knowledge & Skills
Simulations
Ability & Aptitude
Assessment Exercises
Competencies
Development & 360
Personality & Behavior
Biodata & Situational Judgment
"""


def analyze_conversation(messages):

    conversation = ""

    for message in messages:

        conversation += f"{message['role']}: {message['content']}\n"

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": SYSTEM_PROMPT + "\n\nConversation:\n" + conversation
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0
        }
    }

    response = requests.post(
        URL,
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    print(response.status_code)
    print(response.text)
    response.raise_for_status()

    text = response.json()["candidates"][0]["content"]["parts"][0]["text"]

    text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)