def add(a, b):          # 매개변수 a, b를 받아 더한 값을 돌려주는 함수
    return a + b          # return으로 결과를 함수 호출 자리에 돌려줌

result = add(3, 5)        # 인자 3, 5를 넘겨 함수를 호출 (인자 -> 매개변수로 전달됨)
print(f"add(3, 5) 결과: {result}")

def greet(name="손님"):   # 기본값 매개변수 - 인자를 생략하면 "손님"이 자동으로 쓰임
    return f"안녕하세요, {name}님!"

print(greet("김민준"))     # 인자를 넘기면 그 값 사용
print(greet())              # 인자를 생략하면 기본값 "손님" 사용

def is_even(n):            # 조건문과 함수를 함께 사용 - 짝수인지 판별해 불리언을 반환
    return n % 2 == 0        # 비교 연산자 결과(bool)를 그대로 반환

for i in range(1, 6):        # 함수와 반복문을 함께 사용
    print(f"{i}는 짝수인가?: {is_even(i)}")

def do_nothing():            # return이 없는 함수
    print("이 함수는 return이 없습니다.")

none_result = do_nothing()
print(f"return이 없는 함수의 반환값: {none_result}") 