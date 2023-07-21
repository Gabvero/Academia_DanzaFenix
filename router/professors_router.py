from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.professors_schema import ProfessorSchema
from config.db import engine
from model.professors import professors
from typing import List

professor_router = APIRouter()


@professor_router.get("/api/professors", response_model=List[ProfessorSchema])
def get_professors():
    with engine.connect() as conn:
        result = conn.execute(professors.select()).fetchall()

        return result

@professor_router.get("/api/professors/{professor_id}", response_model=ProfessorSchema)
def get_professor(professor_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            professors.select().where(professors.c.id_prof == professor_id)
        ).first()

        return result


@professor_router.post("/api/professors", status_code=HTTP_201_CREATED)
def create_professor(professor_data: ProfessorSchema):
    with engine.connect() as conn:
        new_professor = professor_data.dict()
        conn.execute(professors.insert().values(new_professor))

        return {"message": "Professor created successfully"}


@professor_router.put("/api/professors/{professor_id}", response_model=ProfessorSchema)
def update_professor(professor_data: ProfessorSchema, professor_id: int):
    with engine.connect() as conn:
        conn.execute(
            professors.update().values(professor_data).where(
                professors.c.id_prof == professor_id))

        updated_professor = conn.execute(
            professors.select().where(professors.c.id_prof == professor_id)
        ).first()

        return updated_professor


@professor_router.delete(
    "/api/professors/{professor_id}", status_code=HTTP_204_NO_CONTENT)
def delete_professor(professor_id: int):
    with engine.connect() as conn:
        conn.execute(professors.delete().where(professors.c.id_prof == professor_id))

        return {"message": "Professor deleted successfully"}