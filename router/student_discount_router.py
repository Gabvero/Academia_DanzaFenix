from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.student_discount_schema import StudentDiscountSchema
from config.db import engine
from model.student_discount import student_discount
from typing import List

student_discount_router = APIRouter()


@student_discount_router.get("/api/student_discount", response_model=List[StudentDiscountSchema])
def get_student_discount():
    with engine.connect() as conn:
        result = conn.execute(student_discount.select()).fetchall()

        return result


@student_discount_router.get("/api/student_discount/{student_discount_id}", response_model=StudentDiscountSchema)
def get_student_discount(student_discount_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            student_discount.select().where(student_discount.c.id_discount_student == student_discount_id)
        ).first()

        return result


@student_discount_router.post("/api/student_discount", status_code=HTTP_201_CREATED)
def create_student_discount(student_discount_data: StudentDiscountSchema):
    with engine.connect() as conn:
        new_student_discount = student_discount_data.dict()
        conn.execute(student_discount.insert().values(new_student_discount))

        return Response(status_code=HTTP_201_CREATED)


@student_discount_router.put("/api/student_discount/{student_discount_id}", response_model=StudentDiscountSchema)
def update_student_discount(student_discount_data: StudentDiscountSchema, student_discount_id: int):
    with engine.connect() as conn:
        conn.execute(
            student_discount.update().values(student_discount_data).where(
                student_discount.c.id_discount_student == student_discount_id)
        )

        updated_student_discount = conn.execute(
            student_discount.select().where(student_discount.c.id_discount_student == student_discount_id)
        ).first()

        return updated_student_discount


@student_discount_router.delete("/api/student_discount/{student_discount_id}", status_code=HTTP_204_NO_CONTENT)
def delete_student_discount(student_discount_id: int):
    with engine.connect() as conn:
        conn.execute(student_discount.delete().where(student_discount.c.id_discount_student == student_discount_id))

        return Response(status_code=HTTP_204_NO_CONTENT)