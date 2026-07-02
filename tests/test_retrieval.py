print("Starting retrieval test...")
from services.retriever import search_assessments

queries = [
    "Senior Leadership",
    "Graduate Financial Analyst",
    "Java Developer",
    "Contact Center",
    "Personality Assessment"
]

for query in queries:

    print("=" * 80)
    print("QUERY:", query)
    print("=" * 80)

    results = search_assessments(query)

    for i, assessment in enumerate(results, start=1):

        print(f"\n{i}. {assessment['name']}")
        print(f"Distance: {assessment['distance']:.4f}")
        print(assessment["url"])