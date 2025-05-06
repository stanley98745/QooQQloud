from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime


class CourseTemplateBase(BaseModel):
    title: str
    description: Optional[str] = None
    version: str
    file_url: Optional[HttpUrl] = None  # Unity 可上傳課程 Asset 的網址

class CourseTemplateCreate(CourseTemplateBase):
    uploader_id: int  # FastAPI 端會從 Token 拿 ID，這裡暫保留明示欄位

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "title": "冷媒安裝模擬",
                "description": "模擬冷媒壓力測試的作業流程",
                "version": "v1.0.1",
                "file_url": "https://example.com/assetbundle/cooling-test",
                "uploader_id": 3
            }
        }

class CourseTemplateOut(CourseTemplateBase):
    id: int
    uploaded_at: datetime
    uploader_id: int
    is_active: bool

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "冷媒安裝模擬",
                "description": "模擬冷媒壓力測試的作業流程",
                "version": "v1.0.1",
                "file_url": "https://example.com/assetbundle/cooling-test",
                "uploaded_at": "2025-05-02T14:30:00",
                "uploader_id": 3,
                "is_active": True
            }
        }