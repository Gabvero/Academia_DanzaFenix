from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.class_schema import ClassSchema
from config.db import engine
from schema.discount_schema import DiscountSchema
from model.discount import discount
from typing import List

discounts_router = APIRouter()

@discounts_router.get("/api/discounts", response_model=List[DiscountSchema])
def get_discounts():
    with engine.connect() as conn:
        result = conn.execute(discount.select()).fetchall()

        return result


@discounts_router.get("/api/discounts/{discount_id}", response_model=DiscountSchema)
def get_discount(discount_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            discount.select().where(discount.c.id_discount == discount_id)
        ).first()

        return result


@discounts_router.post("/api/discounts", status_code=HTTP_201_CREATED)
def create_discount(discount_data: DiscountSchema):
    with engine.connect() as conn:
        new_discount = discount_data.dict()
        conn.execute(discount.insert().values(new_discount))

        return {"message": "Discount created successfully"}


@discounts_router.put("/api/discounts/{discount_id}", response_model=DiscountSchema)
def update_discount(discount_data: DiscountSchema, discount_id: int):
    with engine.connect() as conn:
        conn.execute(
            discount.update().values(discount_data).where(
                discount.c.id_discount == discount_id)
        )

        updated_discount = conn.execute(
            discount.select().where(discount.c.id_discount == discount_id)
        ).first()

        return updated_discount


@discounts_router.delete("/api/discounts/{discount_id}", status_code=HTTP_204_NO_CONTENT)
def delete_discount(discount_id: int):
    with engine.connect() as conn:
        conn.execute(discount.delete().where(discount.c.id_discount == discount_id))

        return {"message": "Discount deleted successfully"}