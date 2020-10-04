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
    NAME: ClassVar[str] = 'general'

    name: str
    db: DataBaseEnum = Field(default=DataBaseEnum.SQLITE, title='database')

class DataBaseSection(config.Section):
    NAME: ClassVar[str] = 'database'

    host: str
    port: int = Field(default=8021, gt=0, lt=65535, typeconv=int)
    username: str = 'admin'
    password: str = 'admin'

class AppConfig(config.Config):
    default: DefaultSection
    database: DataBaseSection = Field(default_factory=DataBaseSection)

def test_section_field_schema_mapping() -> None:
    schema = DefaultSection.section_schema()

    assert list(schema.fields.keys()) == ['name', 'db']

    assert schema.name.required
    assert schema.name.name == 'name'
    assert schema.name.typeclass == str
    assert schema.name.typeconv is None
    assert schema.name.help == ''
    assert schema.name.default is None

    assert schema.db.name == 'database'
    assert schema.db.default == DataBaseEnum.SQLITE

    schema = DataBaseSection.section_schema()

    assert schema.host.required
    assert schema.port.typeconv == int
    assert schema.port.default == 8021
    assert schema.username.default == 'admin'
    assert schema.password.default == 'admin'

def test_config_fields_section_type_enforce_with_default() -> None:
    general_section = DefaultSection(name='test field name')

    with pytest.raises(Exception) as excinfo:
        class IllConfig(config.Config):
            general: DefaultSection
            something: str = 'some default to evade init enforce'

        IllConfig(general=general_section)

    assert excinfo

def test_config_fields_section_type_enforce() -> None:
    general_section = DefaultSection(name='test field name')

    with pytest.raises(Exception) as excinfo:
        class IllConfig(config.Config):
            general: DefaultSection
            something: str

        IllConfig(general=general_section, something='test')

    assert excinfo
