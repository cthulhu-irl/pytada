from datetime import datetime
from typing import List

import pytest
from pydantic import Field, ValidationError

from tada.utils.config import Config, Section, TOMLConfigParser

class MandatorySection(Section):
    name: str
    authors: List[str]

class SubSection(Section):
    date: datetime = Field(default_factory=datetime.now)

class OptionalSection(Section):
    magic_num: int = 0
    groups: List[List[str]] = Field(default_factory=list)
    release: SubSection = Field(default_factory=SubSection)

class SomeConfig(Config):
    mandatory: MandatorySection
    optional: OptionalSection = Field(default_factory=OptionalSection)


def test_only_required_fields_valid():
    toml = """
    [mandatory]
    name = "xchg rax, rax"
    authors = ["xorpd"]
    """

    config = TOMLConfigParser.parse(SomeConfig, toml)

    assert config.mandatory.name == "xchg rax, rax"
    assert config.mandatory.authors == ["xorpd"]

def test_all_fields_valid():
    toml = """
    [mandatory]
    name = "Baby Driver"
    authors = ["Jan Krouac"]

    [optional]
    magic_num = 42
    groups = [["Baby Driver"], ["Hitchhiker"], ["debi", "music"]]

    [optional.release]
    date = "2017-1-1"
    """

    config = TOMLConfigParser.parse(SomeConfig, toml)

    assert config.mandatory.name == "Baby Driver"
    assert config.optional.groups == [
        ["Baby Driver"], ["Hitchhiker"], ["debi", "music"]
    ]
    assert config.optional.release.date == datetime(2017, 1, 1)

def test_missing_optoinal_subsection_field():
    toml = """
    [mandatory]
    name = "Fight Club"
    authors = ["Chuck Palahniuk"]

    [optional]
    magic_num = 42
    groups = [["Fight Club"], ["Hitchhiker"], ["debi", "music"]]
    """

    config = TOMLConfigParser.parse(SomeConfig, toml)

    assert config.optional.groups == [
        ["Fight Club"], ["Hitchhiker"], ["debi", "music"]
    ]

    # should equal to datetime.now() but latency might
    # make this assumption false-positive and assertion fail
    assert bool(config.optional.release.date)

def test_missing_mandatory_section_field():
    toml = """
    [optional.release]
    date = "2010-1-1"
    """

    with pytest.raises(ValidationError):
        TOMLConfigParser.parse(SomeConfig, toml)

def test_unknown_section_in_toml():
    toml = """
    [mandatory]
    name = "Sutter Island"
    authors = ["Dennis Lehane"]

    [movie]
    name = "Sutter Island"
    director = ["Martin Scorsese"]
    """

    with pytest.raises(ValidationError):
        TOMLConfigParser.parse(SomeConfig, toml)


def test_missing_field():
    toml = """
    [mandatory]
    name = "Red Dragon"
    """

    with pytest.raises(ValidationError):
        TOMLConfigParser.parse(SomeConfig, toml)


def test_unknown_field_in_section_in_toml():
    toml = """
    [mandatory]
    name = "Red Dragon"
    author = "Thomas Harris"
    """

    with pytest.raises(ValidationError):
        TOMLConfigParser.parse(SomeConfig, toml)
