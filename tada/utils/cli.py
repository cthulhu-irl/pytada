from typing import Type, List

from pydantic import BaseModel

class ARGVCLIParser(object):

    def __init__(self, klass: Type['CLI'], prog: str = ''):
        pass

    def parse(self, argv: List[str]) -> 'CLI':
        pass

    def unparse(self, cli: 'CLI') -> List[str]:
        pass

class Command(BaseModel):
    pass

class CLI(BaseModel):
    pass
