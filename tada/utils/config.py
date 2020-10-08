from typing import Type

from pydantic import BaseModel

class TOMLConfigParser(object):

    @staticmethod
    def parse(klass: Type['Config'], string: str) -> 'Config':
        pass

    @staticmethod
    def unparse(config: 'Config') -> str:
        pass

class Section(BaseModel):

    class Config:
        validate_assignment = True

class Config(BaseModel):
    pass
