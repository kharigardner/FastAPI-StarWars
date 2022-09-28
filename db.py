# this script holds the database connection and crud operations

# importing libraries
from sqlmodel import SQLModel, create_engine, Session, select

database = "starwars.db"

# creating the engine and session

engine = create_engine(f"sqlite:///{database}", echo=True)
db_session = Session(engine)

