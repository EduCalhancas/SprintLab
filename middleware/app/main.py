from fastapi import FastAPI, Request
from app.gitlab import handle_gitlab_event
from app.teams import handle_teams_event

app = FastAPI()

# Rota para receber Webhooks do GitLab
@app.post("/webhook/gitlab")
async def gitlab_webhook(request: Request):
    payload = await request.json()
    response = handle_gitlab_event(payload)
    return {"status": "success", "response": response}
print("Passou")
# Rota para receber eventos do Microsoft Teams
@app.post("/webhook/teams")
async def teams_webhook(request: Request):
    payload = await request.json()
    response = handle_teams_event(payload)
    return {"status": "success", "response": response}
