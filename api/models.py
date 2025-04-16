from pydantic import BaseModel
from typing import Any


class SettingUpdate(BaseModel):
    value: Any
