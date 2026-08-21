# 상수와 샘플 문서 데이터 
# MIN_DOCUMENT_LENGTH = 10 # config.py와 동일한 최소 문서 길이 기준
from pydantic import ValidationError
from app.config import DOCUMENT_DOMAIN, MIN_DOCUMENT_LENGTH
from app.models import Document
from app.schemas import DocumentCreate
from app.exceptions import DocumentNotFoundError, DocumentValidationError
from app.decorators import log_call

# 문서가 여러 건이므로 바깥은 list로 감싸고, 문서 한 건은 여러 필드를 가지므로 dict로 표현
SAMPLE_DOCUMENTS = [
    Document(1, "연차 휴가 신청 절차 안내", "연차 휴가는 최소 3일 전에 신청해야 하며, 팀장 승인 후 확정됩니다.", "HR"),
    Document(2, "사내 네트워크 보안 정책", "사내망 접속 시 VPN을 반드시 사용해야 하며, 비밀번호는 90일마다 변경합니다.", "IT"),
    Document(3, "출장비 정산 가이드", "출장비는 영수증을 첨부해 정산 시스템에 등록하면 익월 급여와 함께 지급됩니다.", "Finance"),
    Document(4, "신규 입사자 온보딩 체크리스트", "입사 첫 주에는 사내 계정 발급, 장비 수령, 필수 교육 이수를 완료해야 합니다.", "HR"),
]

def create_document(raw_data, doc_id):
    # raw_data(dict)를 DocumentCreate로 먼저 검증한 뒤, 통과하면 Document 인스턴스를 만들어 반환
    try:
        validated = DocumentCreate(**raw_data)   # **raw_data - dict의 key들을 그대로 키워드 인자로 펼쳐서 전달
    except ValidationError as error:
        # Pydantic의 ValidationError를 그대로 밖으로 내보내지 않고, 우리 프로젝트의 커스텀 예외로 감싸서 다시 발생
        raise DocumentValidationError(str(error))
    return Document(doc_id, validated.title, validated.content, validated.category)


@log_call   # @데코레이터이름 - def 바로 위에 붙이면 "이 함수 = log_call(이 함수)"와 같은 뜻
def find_document_by_id(documents, doc_id):
    # id가 일치하는 Document를 찾아 반환, 없으면 DocumentNotFoundError를 발생시킴 (예전에는 None을 반환했음)
    for doc in documents:
        if doc.id == doc_id:
            return doc
    raise DocumentNotFoundError(doc_id)   # raise - 여기서 예외를 직접 발생시켜 "찾지 못했다"는 상황을 알림


def list_titles(documents):
    # 문서 목록에서 제목만 뽑아 새로운 list로 반환
    titles = []
    for doc in documents:
        titles.append(doc.title)
    return titles


def get_unique_categories(documents):
    # set은 중복을 자동으로 제거하므로, 카테고리 "종류"만 구하고 싶을 때 적합
    categories = set()
    for doc in documents:
        categories.add(doc.category)
    return categories


def count_by_category(documents):
    # 카테고리별 문서 개수를 dict로 집계 (key: 카테고리, value: 개수)
    counts = {}
    for doc in documents:
        counts[doc.category] = counts.get(doc.category, 0) + 1
    return counts


def find_documents_by_category(documents, category):
    # 특정 category와 일치하는 Document들만 모아 새 list로 반환
    matched = []
    for doc in documents:
        if doc.category == category:
            matched.append(doc)
    return matched


if __name__ == "__main__":
    print(f"[문서 확인] 도메인: {DOCUMENT_DOMAIN}")
    print(f"[문서 확인] 전체 문서 수: {len(SAMPLE_DOCUMENTS)}건")
    print(f"[문서 확인] 문서 목록(Document.__repr__로 출력): {SAMPLE_DOCUMENTS}")
    print(f"[문서 확인] 제목 목록: {list_titles(SAMPLE_DOCUMENTS)}")

    new_doc = create_document(
        {"title": "법인카드 사용 지침", "content": "법인카드는 업무 목적 지출에만 사용합니다.", "category": "Finance"},
        doc_id=5,
    )
    print(f"[문서 확인] 새로 생성된 문서:{new_doc}")

    try:
        create_document({"title": "", "content": "짧음", "category": "HR"}, doc_id=6)   # title 빈 문자열 + content 너무 짧음
    except DocumentValidationError as error:
        print(f"[문서 확인] 예상된 검증 에러:{error}")


    found = find_document_by_id(SAMPLE_DOCUMENTS, 2)
    print(f"[문서 확인] id=2 문서: {found}")

    try:
        find_document_by_id(SAMPLE_DOCUMENTS, 999)      # 존재하지 않는 id -> DocumentNotFoundError 발생
    except DocumentNotFoundError as error:               # 그 예외를 여기서 잡아서 프로그램이 멈추지 않게 처리
        print(f"[문서 확인] 예상된 에러 처리:{error}")


    print(f"[문서 확인] 카테고리 종류: {get_unique_categories(SAMPLE_DOCUMENTS)}")
    print(f"[문서 확인] 카테고리별 개수: {count_by_category(SAMPLE_DOCUMENTS)}")

    for document in SAMPLE_DOCUMENTS:
        if not document.is_long_enough():   # 이제 함수가 아니라 문서 스스로가 판단하는 메서드 호출
            print(f"[경고] '{document.title}' 문서가 최소 길이보다 짧습니다.")
    print("[문서 확인] 모든 문서 길이 점검 완료")

    for document in SAMPLE_DOCUMENTS:
        print(f"[요약]{document.title}:{document.summary()}")