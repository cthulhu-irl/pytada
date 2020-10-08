from typing import Type

from pydantic import BaseModel

class TOMLConfigParser(object):

    def __init__(self, config_factory: Type['Config']):
        pass

    def parse(self, string: str) -> 'Config':
        pass

    def unparse(self, config: 'Config') -> str:
        pass

class Section(BaseModel):
    class Config:
        validate_assignment = True

class Config(BaseModel):
    pass
