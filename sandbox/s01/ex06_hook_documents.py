# [1단계] 문서 한 건에 변수 하나씩 - 4건까지는 그럭저럭 됩니다
doc1_title = "연차 휴가 신청 절차 안내"
doc2_title = "사내 네트워크 보안 정책"
doc3_title = "출장비 정산 가이드"
doc4_title = "신규 입사자 온보딩 체크리스트"

print("[변수 4개 방식] 문서 목록")
print(doc1_title)
print(doc2_title)
print(doc3_title)
print(doc4_title)
print("[변수 4개 방식] 전체 문서 수: 4건 (사람이 직접 세어서 손으로 적은 값)")

# [2단계] 똑같은 데이터를 '한 덩어리'로 묶으면 어떻게 달라지는지 비교해봅니다
doc_titles = [
    "연차 휴가 신청 절차 안내",
    "사내 네트워크 보안 정책",
    "출장비 정산 가이드",
    "신규 입사자 온보딩 체크리스트",
]

print("[묶어서 관리하는 방식] 문서 목록")
for title in doc_titles:
    print(title)
print(f"[묶어서 관리하는 방식] 전체 문서 수: {len(doc_titles)}건 (문서가 40건이 되어도 이 줄은 그대로)")