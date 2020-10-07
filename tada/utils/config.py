from pydantic import BaseModel

class Section(BaseModel):
    class Config:
        validate_assignment = True

class Config(BaseModel):
    pass
