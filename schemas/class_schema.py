from pydantic import BaseModel
from typing import Optional

class ClassBase(BaseModel):
    class_ID:str
    class_name: str
    year: int

    class Config:
        json_schema_extra = {
            "example": {
                "class_ID": "11300100B021",
                "class_name": "113年冷凍空調裝修乙級第二期班A",
                "year": 113
            }
        }

class ClassCreate(ClassBase):
    pass

class ClassUpdate(BaseModel):
    class_ID: str
    class_name: str
    year: int

    class Config:
        json_schema_extra = {
            "example": {
                "class_ID": "11300100B021",
                "class_name": "113年冷凍空調裝修乙級第二期班A",
                "year": 113
            }
        }

class ClassResponse(ClassBase):
    class_ID: str
    class_name: str
    year: int

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "class_ID": "11300100B021",
                "class_name": "113年冷凍空調裝修乙級第二期班A",
                "year": 113
            }
        }
