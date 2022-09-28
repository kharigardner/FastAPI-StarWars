# this is a sample API built with FastAPI, performing crud operations on a sample sqllite database representing the star wars universe

from fastapi import FastAPI
from db import db_session
from models import Character
from crud import *
from typing import List

app = FastAPI(
    title="Star Wars API",
    description="This is a sample API built with FastAPI, performing crud operations on a sample sqllite database representing the star wars universe",
    version="0.1.0",
)
#TODO: add more description and settings to the API initialization


@app.get("/")
async def root():
    return {"message": "Hello! This is a sample API built with FastAPI, performing crud operations on a sample sqllite database representing the star wars universe"}

@app.get("/health")
async def health():
    return {"status": "ok"}

# character endpoints
# endpoint with path parameters
@app.post("/character", response_model=Character)
async def create_character(character: Character):
    try:
        db_session.add(character)
        db_session.commit()
        db_session.refresh(character)
        return character
    except:
        return "{message: 'character creation failed'}"

@app.get("/character/{character_id}", response_model=Character)
async def read_character(character_id: int):
    try:
        return db_session.get(Character, character_id)
    except:
        return "{message: 'character not found'}"

@app.get("/character", response_model=List[Character])
async def read_all_characters():
    try:
        return db_session.exec(select(Character)).all()
    except:
        return "{message: 'no characters found'}"

@app.put("/character/{character_id}", response_model=Character)
async def update_character(character_id: int, character: Character):
    try:
        db_session.add(character)
        db_session.commit()
        db_session.refresh(character)
        return character
    except:
        return "{message: 'character update failed'}"

@app.delete("/character/{character_id}", response_model=Character)
async def delete_character(character_id: int):
    try:
        character = db_session.get(Character, character_id)
        db_session.delete(character)
        db_session.commit()
        return character
    except Exception as e:
        print(e)
        return "{message: 'character deletion failed'}"

@app.patch("/character/{character_id}", response_model=Character)
async def patch_character(character_id: int, character: Character):
    try:
        db_session.add(character)
        db_session.commit()
        db_session.refresh(character)
        return character
    except:
        return "{message: 'character patch failed'}"

@app.on_event("shutdown")
async def shutdown_event():
    return db_session.close()


