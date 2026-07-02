from services.decision_engine import decide
analysis = {
    "intent":"recommend",
    "out_of_scope":False,
    "context":{
        "role":None,
        "job_level":None,
        "purpose":None,
        "skills":[],
        "language":None,
        "assessment_categories":[],
        "assessment_names":[]
    }
}

print(decide(analysis))