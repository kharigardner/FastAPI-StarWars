from sqlmodel import SQLModel, create_engine, Session, select, Field
from typing import List, Optional, Any, Dict
from fastapi_camelcase import CamelModel

# initalizaing the camel case instance to automatically convert the json response to camel case
camel = CamelModel()

# defining the models, luckily with sqlmodel it gets really easy

class Character(SQLModel, table=True):
    # creating a identity id column for the character, this is the primary key
    character_id: Optional[int] = Field(default=None, primary_key=True)
    first_name: Optional[str]
    last_name: Optional[str]
    birthdate_bby: Optional[str]
    deathdate_bby: Optional[str]
    species: Optional[str]
    faction: Optional[str]
    force_alignment: Optional[str]
    team: Optional[str]
    media: Optional[str] = Field(default={})
    weapons: Optional[str] = Field(default={})
    ships: Optional[str] = Field(default={})
    # weapons and ships are dictionaries with id and name as key/value pairs, stored as string in sqllite since sqllite does not support dictionaries