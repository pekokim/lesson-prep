# for 반복문 - range(5)는 0,1,2,3,4 다섯 개의 숫자를 차례로 꺼내줌
total = 0   # 합계를 누적할 변수 (반복문 시작 전에 반드시 초기값을 정해둬야 함)
for i in range(1, 6):   # range(1, 6) - 1부터 5까지 (6은 포함되지 않음)
    total = total + i    # 매 회차마다 i를 total에 누적
print(f"1부터 5까지의 합: {total}")

# [선택] continue - 짝수는 건너뛰고 홀수만 출력
for n in range(1, 11):    # 1부터 10까지
    if n % 2 == 0:         # 나머지 연산자로 짝수 판별
        continue            # 이번 회차만 건너뛰고 다음 숫자로 넘어감
    print(f"홀수: {n}")

# [선택] break - 특정 값을 찾으면 즉시 반복 중단
target = 7
for n in range(1, 11):
    if n == target:
        print(f"{target}을 찾았습니다! 반복을 즉시 종료합니다.")
        break               # 반복문을 완전히 멈춤 (이후 숫자는 검사하지 않음)

# while 반복문 - 조건이 참인 동안만 반복
count = 0
while count < 3:            # count가 3보다 작은 동안 반복
    print(f"while 반복 {count}번째")
    count = count + 1        # 조건이 언젠가 거짓이 되도록 반드시 값을 바꿔줘야 무한 루프를 피할 수 있음