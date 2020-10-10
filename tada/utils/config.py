from typing import Type

import toml
from pydantic import BaseModel

class TOMLConfigParser(object):

    @staticmethod
    def parse(klass: Type['Config'], string: str) -> 'Config':
        return klass(**toml.loads(string))

    @staticmethod
    def unparse(config: 'Config') -> str:
        return toml.dumps(config.dict())

class Section(BaseModel):

    class Config:
        validate_assignment = True

class Config(BaseModel):
    pass
