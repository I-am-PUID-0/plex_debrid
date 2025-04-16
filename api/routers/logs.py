from fastapi import APIRouter

router = APIRouter()


@router.get("/logs/{process_name}")
def get_logs(process_name: str):
    return {"message": f"Logs for {process_name} (not yet implemented)"}
