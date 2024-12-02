import requests

TEAMS_WEBHOOK_URL = "your_teams_incoming_webhook_url"
TEAMS_APP_ID = "your_teams_app_id"
TEAMS_APP_SECRET = "your_teams_app_secret"

def handle_teams_event(payload):
    # Processar eventos recebidos do Teams
    user_action = payload.get("action", "")
    
    if user_action == "move_task":
        return process_task_update(payload)
    else:
        return {"message": "Event not handled"}

def process_task_update(data):
    task_id = data["task"]["id"]
    new_status = data["task"]["status"]
    return {"message": f"Task {task_id} updated to {new_status}."}

def send_to_teams(message):
    headers = {"Content-Type": "application/json"}
    payload = {"text": message}
    response = requests.post(TEAMS_WEBHOOK_URL, json=payload, headers=headers)
    return response.json()
