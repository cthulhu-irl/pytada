from pydantic import BaseModel

from .config import Section

class Command(Section):
    name: str

class CLI(BaseModel):
    pass
