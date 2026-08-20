MIN_DOCUMENT_LENGTH = 10   # L02에서 만든 project/app/config.py의 같은 이름 값을 sandbox에서도 재현

def count_characters(text):        # 문자열의 글자 수를 반복문으로 직접 세어보는 함수 (len()을 쓰지 않고 원리 확인용)
    count = 0                        # 글자 수를 누적할 변수, 반복 시작 전 0으로 초기화
    for character in text:            # 문자열은 한 글자씩 순회 가능(Iterable) - 문자를 하나씩 꺼냄
        count = count + 1              # 글자를 하나 볼 때마다 누적 카운트 증가
    return count                       # 다 센 뒤 최종 글자 수를 반환 (반환값은 언제나 하나)

def check_document_length(text, minimum=MIN_DOCUMENT_LENGTH):   # 기본값 매개변수로 최소 글자 수 지정
    length = count_characters(text)     # 위에서 만든 함수를 그대로 재사용(함수는 다른 함수 안에서도 호출 가능)
    if length < minimum:                  # 조건문 - 기준보다 짧으면
        return False                       # 통과하지 못했다는 뜻으로 False를 반환
    else:                                  # 기준을 만족하면
        return True                         # 통과했다는 뜻으로 True를 반환

def report_document(number, text):    # 문서 하나를 검사하고 결과를 화면에 출력하는 함수
    length = count_characters(text)     # 글자 수 계산 (위 함수 재사용)
    is_ok = check_document_length(text)  # 통과 여부 판정 (위 함수 재사용)
    print(f"[문서 {number}] 글자 수: {length}, 통과 여부: {is_ok}")
    if not is_ok:                         # not 연산자 - is_ok가 False일 때 참
        print(f"  └ '{text}'는 최소 글자 수({MIN_DOCUMENT_LENGTH}자)보다 짧아 이번 배치에서는 건너뜁니다.")
    else:
        print("  └ 처리를 계속 진행합니다.")

# 검사해볼 문서 후보 3개 (여러 값을 한 상자에 담는 자료구조는 L04에서 배우므로, 지금은 변수 3개로 준비)
doc_a = "회의록: 오늘 논의된 안건은 세 가지입니다."
doc_b = "짧은 문서"
doc_c = "이 문서는 사내 정책에 대한 충분히 긴 설명을 담고 있는 문서입니다."

# 함수로 묶어두었기 때문에, 문서마다 같은 코드를 복사할 필요 없이 이름만 세 번 부르면 됨
report_document(1, doc_a)
report_document(2, doc_b)
report_document(3, doc_c)