# dataclasses for halftest

import datetime
import typing


import dataclasses
from half_orm.relation import DC_Relation
from half_orm.field import Field

@dataclasses.dataclass
class DC_ActorPerson(DC_Relation):
    id: int = dataclasses.field(default=None)
    first_name: str = dataclasses.field(default=None)
    last_name: str = dataclasses.field(default=None)
    birth_date: datetime.date = dataclasses.field(default=None)
    def __post_init__(self):
        self.id: Field = None
        self.first_name: Field = None
        self.last_name: Field = None
        self.birth_date: Field = None

@dataclasses.dataclass
class DC_BlogComment(DC_Relation):
    id: int = dataclasses.field(default=None)
    content: str = dataclasses.field(default=None)
    post_id: int = dataclasses.field(default=None)
    author_id: int = dataclasses.field(default=None)
    column5: str = dataclasses.field(default=None)
    tags: str = dataclasses.field(default_factory=list)
    def __post_init__(self):
        self.id: Field = None
        self.content: Field = None
        self.post_id: Field = None
        self.author_id: Field = None
        self.column5: Field = None
        self.tags: Field = None

@dataclasses.dataclass
class DC_BlogEvent(DC_Relation):
    id: int = dataclasses.field(default=None)
    title: str = dataclasses.field(default=None)
    content: str = dataclasses.field(default=None)
    author_first_name: str = dataclasses.field(default=None)
    author_last_name: str = dataclasses.field(default=None)
    author_birth_date: datetime.date = dataclasses.field(default=None)
    data: typing.Any = dataclasses.field(default=None)
    begin: datetime.datetime = dataclasses.field(default=None)
    end: datetime.datetime = dataclasses.field(default=None)
    location: str = dataclasses.field(default=None)
    def __post_init__(self):
        self.id: Field = None
        self.title: Field = None
        self.content: Field = None
        self.author_first_name: Field = None
        self.author_last_name: Field = None
        self.author_birth_date: Field = None
        self.data: Field = None
        self.begin: Field = None
        self.end: Field = None
        self.location: Field = None

@dataclasses.dataclass
class DC_BlogPost(DC_Relation):
    id: int = dataclasses.field(default=None)
    title: str = dataclasses.field(default=None)
    content: str = dataclasses.field(default=None)
    author_first_name: str = dataclasses.field(default=None)
    author_last_name: str = dataclasses.field(default=None)
    author_birth_date: datetime.date = dataclasses.field(default=None)
    data: typing.Any = dataclasses.field(default=None)
    def __post_init__(self):
        self.id: Field = None
        self.title: Field = None
        self.content: Field = None
        self.author_first_name: Field = None
        self.author_last_name: Field = None
        self.author_birth_date: Field = None
        self.data: Field = None

@dataclasses.dataclass
class DC_BlogViewPostComment(DC_Relation):
    post_title: str = dataclasses.field(default=None)
    author_post_id: int = dataclasses.field(default=None)
    author_post_first_name: str = dataclasses.field(default=None)
    author_post_last_name: str = dataclasses.field(default=None)
    comment_id: int = dataclasses.field(default=None)
    comment_content: str = dataclasses.field(default=None)
    post_id: int = dataclasses.field(default=None)
    author_comment_id: int = dataclasses.field(default=None)
    author_comment_first_name: str = dataclasses.field(default=None)
    author_comment_last_name: str = dataclasses.field(default=None)
    def __post_init__(self):
        self.post_title: Field = None
        self.author_post_id: Field = None
        self.author_post_first_name: Field = None
        self.author_post_last_name: Field = None
        self.comment_id: Field = None
        self.comment_content: Field = None
        self.post_id: Field = None
        self.author_comment_id: Field = None
        self.author_comment_first_name: Field = None
        self.author_comment_last_name: Field = None
