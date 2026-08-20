# 상수와 샘플 문서 데이터 
# MIN_DOCUMENT_LENGTH = 10 # config.py와 동일한 최소 문서 길이 기준

from app.config import DOCUMENT_DOMAIN, MIN_DOCUMENT_LENGTH
from app.models import Document

# 문서가 여러 건이므로 바깥은 list로 감싸고, 문서 한 건은 여러 필드를 가지므로 dict로 표현
SAMPLE_DOCUMENTS = [
    Document(1, "연차 휴가 신청 절차 안내", "연차 휴가는 최소 3일 전에 신청해야 하며, 팀장 승인 후 확정됩니다.", "HR"),
    Document(2, "사내 네트워크 보안 정책", "사내망 접속 시 VPN을 반드시 사용해야 하며, 비밀번호는 90일마다 변경합니다.", "IT"),
    Document(3, "출장비 정산 가이드", "출장비는 영수증을 첨부해 정산 시스템에 등록하면 익월 급여와 함께 지급됩니다.", "Finance"),
    Document(4, "신규 입사자 온보딩 체크리스트", "입사 첫 주에는 사내 계정 발급, 장비 수령, 필수 교육 이수를 완료해야 합니다.", "HR"),
]

def find_document_by_id(documents, doc_id):
    # id가 일치하는 Document 하나를 찾아 반환, 없으면 None (dict의 doc["id"] 대신 doc.id로 접근)
    for doc in documents:
        if doc.id == doc_id:
            return doc
    return None


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

def summary(self, length=20):
    # content가 length자보다 길면 잘라서 "..."를 붙이고, 아니면 그대로 반환 (L03에서 배운 if 재사용)
    if len(self.content) > length:
        return self.content[:length] + "..."   # 슬라이싱(L04)으로 앞부분만 잘라냄
    return self.content

if __name__ == "__main__":
    print(f"[문서 확인] 도메인: {DOCUMENT_DOMAIN}")
    print(f"[문서 확인] 전체 문서 수: {len(SAMPLE_DOCUMENTS)}건")
    print(f"[문서 확인] 문서 목록(Document.__repr__로 출력): {SAMPLE_DOCUMENTS}")
    print(f"[문서 확인] 제목 목록: {list_titles(SAMPLE_DOCUMENTS)}")

    found = find_document_by_id(SAMPLE_DOCUMENTS, 2)
    print(f"[문서 확인] id=2 문서: {found}")

    print(f"[문서 확인] 카테고리 종류: {get_unique_categories(SAMPLE_DOCUMENTS)}")
    print(f"[문서 확인] 카테고리별 개수: {count_by_category(SAMPLE_DOCUMENTS)}")

    for document in SAMPLE_DOCUMENTS:
        if not document.is_long_enough():   # 이제 함수가 아니라 문서 스스로가 판단하는 메서드 호출
            print(f"[경고] '{document.title}' 문서가 최소 길이보다 짧습니다.")
    print("[문서 확인] 모든 문서 길이 점검 완료")
    
    for document in SAMPLE_DOCUMENTS:
        print(f"[요약]{document.title}:{document.summary()}")