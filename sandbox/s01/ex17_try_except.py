numbers = {"apple": 10, "banana": 0}

# 기본 try/except - try 블록에서 에러가 나면 프로그램이 멈추지 않고 except 블록으로 넘어감
try:
    result = 10 / numbers["banana"]   # 0으로 나누기 -> ZeroDivisionError 발생
except ZeroDivisionError as error:
    print(f"0으로 나눌 수 없습니다:{error}")

# 여러 종류의 예외를 각각 다르게 처리하기
try:
    result = 10 / numbers["cherry"]   # "cherry"라는 key가 없음 -> KeyError 발생
except ZeroDivisionError as error:
    print(f"0으로 나눌 수 없습니다:{error}")
except KeyError as error:
    print(f"존재하지 않는 key입니다:{error}")

# else/finally까지 포함한 전체 구조
try:
    result = 10 / numbers["apple"]     # 정상적으로 계산되는 경우
except ZeroDivisionError as error:
    print(f"0으로 나눌 수 없습니다:{error}")
else:
    print(f"계산 성공, 결과:{result}")   # else - try 블록에서 에러가 하나도 안 났을 때만 실행
finally:
    print("계산 시도가 끝났습니다.")        # finally - 에러가 나든 안 나든 항상 마지막에 실행