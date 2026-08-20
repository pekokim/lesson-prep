class DocumentError(Exception):
    """이 프로젝트의 문서 관련 에러들이 공통으로 물려받는 기본 예외 (Exception을 상속)."""
    pass


class DocumentNotFoundError(DocumentError):
    """요청한 id에 해당하는 문서를 찾지 못했을 때 발생시키는 예외."""

    def __init__(self, doc_id):
        self.doc_id = doc_id                                   # 어떤 id를 찾다가 못 찾았는지 함께 저장
        super().__init__(f"문서를 찾을 수 없습니다 (id={doc_id})")   # 부모(Exception)의 __init__을 호출해 메시지 등록


class DocumentValidationError(DocumentError):
    """문서 필드 값(title, content 등)이 유효하지 않을 때 발생시키는 예외."""
    pass