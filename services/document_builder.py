def build_document(assessment: dict):
    document = f"""
Assessment Name:
{assessment.get("name", "")}

Description:
{assessment.get("description", "")}

Suitable Job Levels:
{", ".join(assessment.get("job_levels", []))}

Assessment Categories:
{", ".join(assessment.get("keys", []))}

Languages:
{", ".join(assessment.get("languages", []))}

Duration:
{assessment.get("duration", "Not Specified")}

Remote Testing:
{assessment.get("remote", "Unknown")}

Adaptive:
{assessment.get("adaptive", "Unknown")}
""".strip()

    metadata = {
        "entity_id": str(assessment.get("entity_id")),
        "name": assessment.get("name"),
        "url": assessment.get("link"),
        "duration": assessment.get("duration"),
        "remote": assessment.get("remote"),
        "adaptive": assessment.get("adaptive"),
        "keys": ",".join(assessment.get("keys", []))
    }

    return document, metadata