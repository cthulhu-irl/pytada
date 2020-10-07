from pydantic import BaseModel

from .config import Section

class Command(Section):
    pass

class CLI(BaseModel):
    pass
