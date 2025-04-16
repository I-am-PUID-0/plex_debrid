from fastapi import APIRouter

router = APIRouter()


@router.post("/oauth/start/{service}")
def start_oauth(service: str):
    return {"message": f"OAuth start for {service} (not yet implemented)"}


@router.get("/oauth/poll/{service}")
def poll_oauth(service: str):
    return {"message": f"OAuth poll for {service} (not yet implemented)"}
