from services.conversation_analyzer import analyze_conversation

messages = [
    {
        "role": "user",
        "content": "I need an assessment for hiring a Java Developer."
    }
]

result = analyze_conversation(messages)

print(result)