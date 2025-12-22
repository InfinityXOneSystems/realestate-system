from executors.pubsub import publish
from executors.workspace import handle_workspace
from executors.crawler import handle_crawler
from intelligence.leads.loan_leads import generate_leads

def dispatch(payload):
    action = payload.get("action")

    if action == "loan_leads":
        return generate_leads(payload)

    if action in ["send_email", "schedule_meeting", "voice_call"]:
        return handle_workspace(payload)

    if action in ["crawl", "ingest"]:
        return handle_crawler(payload)

    if action in ["async", "queue"]:
        return publish(payload)

    return {"error": "Unknown action"}, 400
