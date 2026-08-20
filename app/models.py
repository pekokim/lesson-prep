from app.config import MIN_DOCUMENT_LENGTH   # L05에서 정리한 대로, 설정값은 config.py에서 가져와 재사용


class Document:
    """캡스톤 프로젝트에서 문서 한 건을 표현하는 클래스 (L04·L05의 dict 표현을 대체)."""

    def __init__(self, id, title, content, category):
        # __init__ - Document(...)를 호출해 인스턴스를 만드는 순간 자동으로 실행되는 특별한 메서드
        self.id = id            # self.xxx = 값 -> 이 인스턴스만의 값(인스턴스 속성)으로 저장
        self.title = title
        self.content = content
        self.category = category

    def is_long_enough(self, minimum=MIN_DOCUMENT_LENGTH):
        # 인스턴스 메서드 - self로 이 문서 자신의 content에 접근 (L04의 함수를 클래스 메서드로 이동)
        return len(self.content) >= minimum

    def to_dict(self):
        # 이 문서를 dict로 변환 (JSON으로 저장하기 전 단계, storage.py에서 사용)
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "category": self.category,
        }

    def __repr__(self):
        # __repr__ - 이 객체를 print()하거나 화면에 출력할 때 보여줄 문자열을 정하는 특별한 메서드
        return f"Document(id={self.id}, title={self.title!r}, category={self.category!r})"

    def summary(self, length=20):
        # content가 length자보다 길면 잘라서 "..."를 붙이고, 아니면 그대로 반환 (L03에서 배운 if 재사용)
        if len(self.content) > length:
            return self.content[:length] + "..."   # 슬라이싱(L04)으로 앞부분만 잘라냄
        return self.content