from fastapi import APIRouter, HTTPException
from settings import settings_list

router = APIRouter()


@router.get("/")
def get_all_settings():
    result = []
    for category, items in settings_list:
        result.append({
            "category": category,
            "settings": [s.to_dict() for s in items]
        })
    return result


@router.get("/{key}")
def get_setting_by_key(key: str):
    for _, items in settings_list:
        for s in items:
            if s.key == key:
                return s.to_dict()
    raise HTTPException(status_code=404, detail=f"Setting '{key}' not found")
