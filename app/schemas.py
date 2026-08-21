from pydantic import BaseModel, Field
from app.config import MIN_DOCUMENT_LENGTH


class DocumentCreate(BaseModel):
    """새 문서를 만들 때 들어오는 값을 검증하는 스키마 (나중에 FastAPI 요청 바디로 그대로 재사용됨)."""

    title: str = Field(min_length=1, description="문서 제목, 빈 문자열 불가")
    content: str = Field(min_length=MIN_DOCUMENT_LENGTH, description="문서 본문, 최소 길이는 config.py 기준")
    category: str = Field(min_length=1, description="문서 카테고리")
    