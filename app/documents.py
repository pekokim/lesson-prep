# 상수와 샘플 문서 데이터 
# MIN_DOCUMENT_LENGTH = 10 # config.py와 동일한 최소 문서 길이 기준

from app.config import DOCUMENT_DOMAIN, MIN_DOCUMENT_LENGTH

# 문서가 여러 건이므로 바깥은 list로 감싸고, 문서 한 건은 여러 필드를 가지므로 dict로 표현
SAMPLE_DOCUMENTS = [
    {
        "id": 1,
        "title": "연차 휴가 신청 절차 안내",
        "content": "연차 휴가는 최소 3일 전에 신청해야 하며, 팀장 승인 후 확정됩니다.",
        "category": "HR",   # 카테고리 라벨은 여러 문서에서 반복 사용되는 값이라 영어로 통일
    },
    {
        "id": 2,
        "title": "사내 네트워크 보안 정책",
        "content": "사내망 접속 시 VPN을 반드시 사용해야 하며, 비밀번호는 90일마다 변경합니다.",
        "category": "IT",
    },
    {
        "id": 3,
        "title": "출장비 정산 가이드",
        "content": "출장비는 영수증을 첨부해 정산 시스템에 등록하면 익월 급여와 함께 지급됩니다.",
        "category": "Finance",
    },
    {
        "id": 4,
        "title": "신규 입사자 온보딩 체크리스트",
        "content": "입사 첫 주에는 사내 계정 발급, 장비 수령, 필수 교육 이수를 완료해야 합니다.",
        "category": "HR",
    },
    { 
        "id": 5, 
        "title": "법인카드 사용 지침", 
        "content": "법인카드는 업무 목적 지출에만 사용하며, 사용 후 3일 내 영수증을 제출합니다.", 
        "category": "Finance",
    },
]

def find_document_by_id(documents, doc_id):
    # id가 일치하는 문서 하나를 찾아 dict로 반환, 없으면 None (L03에서 배운 for + if 재사용)
    for doc in documents:
        if doc["id"] == doc_id:
            return doc
    return None


def list_titles(documents):
    # 문서 목록에서 제목만 뽑아 새로운 list로 반환
    titles = []
    for doc in documents:
        titles.append(doc["title"])
    return titles

def get_unique_categories(documents):
    # set은 중복을 자동으로 제거하므로, 카테고리 "종류"만 구하고 싶을 때 적합
    categories = set()
    for doc in documents:
        categories.add(doc["category"])
    return categories

def count_by_category(documents):
    # 카테고리별 문서 개수를 dict로 집계 (key: 카테고리, value: 개수)
    counts = {}
    for doc in documents:
        category = doc["category"]
        counts[category] = counts.get(category, 0) + 1   # 이미 있던 카테고리면 +1, 처음이면 0에서 시작
    return counts


def is_document_long_enough(doc, minimum=MIN_DOCUMENT_LENGTH):
    # 문서 content의 길이가 최소 기준을 넘는지 판단 (기본값은 위에서 정의한 MIN_DOCUMENT_LENGTH)
    return len(doc["content"]) >= minimum


if __name__ == "__main__":
    print(f"[문서 확인] 도메인: {DOCUMENT_DOMAIN}") # 추가 
    print(f"[문서 확인] 전체 문서 수: {len(SAMPLE_DOCUMENTS)}건")
    print(f"[문서 확인] 제목 목록: {list_titles(SAMPLE_DOCUMENTS)}")

    found = find_document_by_id(SAMPLE_DOCUMENTS, 2)
    print(f"[문서 확인] id=2 문서: {found}")

    print(f"[문서 확인] 카테고리 종류: {get_unique_categories(SAMPLE_DOCUMENTS)}")
    print(f"[문서 확인] 카테고리별 개수: {count_by_category(SAMPLE_DOCUMENTS)}")

    # L03에서 배운 for + if를 그대로 활용해 모든 문서의 길이를 점검
    for document in SAMPLE_DOCUMENTS:
        if not is_document_long_enough(document):
            print(f"[경고] '{document['title']}' 문서가 최소 길이({MIN_DOCUMENT_LENGTH}자)보다 짧습니다.")
    print("[문서 확인] 모든 문서 길이 점검 완료")