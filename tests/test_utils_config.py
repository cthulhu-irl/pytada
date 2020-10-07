import enum
from typing import Literal, ClassVar

import pytest
from pydantic import Field

from tada.utils import config

class DataBaseEnum(str, enum.Enum):
    SQLITE = 'sqlite'
    MYSQL = 'mysql'
    POSTGRESQL = 'postgres'

class DefaultSection(config.Section):
    name: str
    db: DataBaseEnum = Field(default=DataBaseEnum.SQLITE, title='database')

class DataBaseSection(config.Section):
    host: str
    port: int = Field(default=8021, gt=0, lt=65535, typeconv=int)
    username: str = 'admin'
    password: str = 'admin'

class AppConfig(config.Config):
    default: DefaultSection
    database: DataBaseSection

def test_instantiation() -> None:
    default_section = DefaultSection(name='test')
    db_section = DataBaseSection(host='localhost')

    with pytest.raises(Exception):
        AppConfig(default=default_section)

    config = AppConfig(default=default_section, database=db_section)

    assert config.default.name == 'test'
    assert config.database.host == 'localhost'
