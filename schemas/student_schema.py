from pydantic import BaseModel

class StudentBase(BaseModel):
    student_ID: str
    student_name: str

class StudentCreate(StudentBase):
    student_ID: str
    student_name: str
    class_ID: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "student_ID": "141001002",
                "student_name": "章學酉",
                "class_ID": "11400100B012"
            }
        }

class StudentUpdate(StudentBase):
    pass

class StudentResponse(StudentBase):
    student_ID: str
    student_name: str
    class_ID: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "student_ID": "141001002",
                "student_name": "章學酉",
                "class_ID": "11400100B012"
            }
        }
