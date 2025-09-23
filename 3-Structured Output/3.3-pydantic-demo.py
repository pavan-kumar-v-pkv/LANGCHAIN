from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "John Doe"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5.0, description="CGPA must be a decimal value between 0 and 10")

new_student = {'name': 'Lightning McQueen', 'age': 5, 'email': 'lightning@cars.com', 'cgpa': 9.5}
student = Student(**new_student)
student_dict = dict(student)
student_json = student.model_dump_json()
print(student_dict['age'])
print(student_dict['cgpa'])
print(student_json)