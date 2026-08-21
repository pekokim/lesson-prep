def greet(name: str) -> str:   # name: str - "이 자리에는 문자열이 올 예정"이라는 메모, -> str은 "돌려주는 값도 문자열 예정"이라는 메모
    return f"안녕하세요{name}님"


print(greet("김민준"))   # 메모대로 문자열을 넣은 경우
print(greet(123))        # 메모와 다른 정수를 넣었지만... 과연 에러가 날까요? -> 에러 안남