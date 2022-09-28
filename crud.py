# this script contains the basic crud operations using sqlmodel on the db
from sqlmodel import SQLModel, Session
def create(model: SQLModel, db_session: Session):
    db_session.add(model)
    db_session.commit()
    db_session.refresh(model)
    return model

def read(model_identifier: any, db_session: Session):
    return db_session.get(model_identifier)

def read_all(model: SQLModel, db_session: Session):
    return db_session.exec(select(model)).all()

def update(model: SQLModel, db_session: Session):
    db_session.add(model)
    db_session.commit()
    db_session.refresh(model)
    return model

def delete(model_identifier: any, db_session: Session):
    model = db_session.get(model_identifier)
    db_session.delete(model)
    db_session.commit()
    return model