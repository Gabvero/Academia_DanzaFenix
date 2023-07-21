from pydantic import BaseModel
from typing import Optional

class StudentDiscountSchema(BaseModel):
    id_student_discount: Optional[int] = None
    id_discount: Optional[int]
    id_student: int