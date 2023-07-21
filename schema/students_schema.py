from pydantic import BaseModel
from typing import Optional

class StudentSchema(BaseModel):
    id_student: Optional[int] = None
    id_user: int
    id_inscription: int
    name_student: str
    last_name_student: str
    age: int
    phone: str
    email: str