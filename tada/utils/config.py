from typing import ClassVar

from pydantic import BaseModel

class Section(BaseModel):
    NAME: ClassVar[str] = "default"

    class Config:
        validate_assignment = True

class Config(BaseModel):
    pass
