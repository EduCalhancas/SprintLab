import gitlab

# Configurar conexão com GitLab
GITLAB_URL = "https://gitlab.com/api/v4"
GITLAB_TOKEN = "glpat-nyk49dZRjWVwgyffT5f3"

gl = gitlab.Gitlab(GITLAB_URL, private_token=GITLAB_TOKEN)

def handle_gitlab_event(payload):
    event_type = payload.get("object_kind", "")
    
    if event_type == "issue":
        return process_issue_event(payload)
    elif event_type == "merge_request":
        return process_merge_request_event(payload)
    else:
        return {"message": "Event type not handled"}

def process_issue_event(data):
    issue_title = data["object_attributes"]["title"]
    project_id = data["project"]["id"]
    return {"message": f"Issue '{issue_title}' in project {project_id} processed."}

def process_merge_request_event(data):
    mr_title = data["object_attributes"]["title"]
    project_id = data["project"]["id"]
    return {"message": f"Merge request '{mr_title}' in project {project_id} processed."}
