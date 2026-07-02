from services.conversation_analyzer import analyze_conversation
from services.decision_engine import decide
from services.retriever import search_assessments
from services.response_generator import generate_response

TEST_TYPE_MAP = {
    "Knowledge & Skills": "K",
    "Personality & Behavior": "P",
    "Ability & Aptitude": "A",
    "Simulations": "S",
    "Assessment Exercises": "E",
    "Competencies": "C",
    "Development & 360": "D",
    "Biodata & Situational Judgment": "B"
}


def process_chat(messages):

    analysis = analyze_conversation(messages)

    decision = decide(analysis)

    if decision["action"] == "ask":
        return {
            "reply": decision["question"],
            "recommendations": [],
            "end_of_conversation": False
        }

    if decision["action"] == "refuse":
        return {
            "reply": "I can only answer questions related to SHL assessments.",
            "recommendations": [],
            "end_of_conversation": True
        }

    context = analysis["context"]

    query_parts = []

    if context["role"]:
        query_parts.append(context["role"])

    if context["purpose"]:
        query_parts.append(context["purpose"])

    if context["skills"]:
        query_parts.extend(context["skills"])

    if context["assessment_categories"]:
        query_parts.extend(context["assessment_categories"])

    query = " ".join(query_parts)

    assessments = search_assessments(query)

    reply = generate_response(messages, assessments)
    
    recommendations = []
    
    for assessment in assessments[:5]:

        first_key =""

    if assessment.get("keys"):
        keys = assessment.get("keys", [])

        first_key = keys[0].strip() if keys else ""
        print(assessment["keys"])
        print(first_key)


    recommendations.append({
        "name": assessment["name"],
        "url": assessment["url"],
        "test_type": TEST_TYPE_MAP.get(first_key, "O")
    })

    
    return {
        "reply": reply,
        "recommendations": recommendations,
        "end_of_conversation": False
    }