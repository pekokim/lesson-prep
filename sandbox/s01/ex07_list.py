fruits = ["apple", "banana", "cherry"]   # list - 여러 값을 순서대로 묶어 담는 자료구조([]로 만듦)
print(f"전체 리스트: {fruits}")
print(f"길이: {len(fruits)}")            # len() - 안에 담긴 항목이 몇 개인지 세어줌

print(f"첫 번째 항목(인덱스 0): {fruits[0]}")   # 인덱싱 - 0부터 시작하는 위치 번호로 값 하나를 꺼냄
print(f"마지막 항목(인덱스 -1): {fruits[-1]}")   # 음수 인덱스 - 뒤에서부터 세는 위치 번호

fruits.append("durian")                 # append() - 리스트 맨 뒤에 새 항목을 추가 (문서가 늘어나는 상황과 같음)
print(f"append 후: {fruits}")

fruits.remove("banana")                 # remove(값) - 그 값을 앞에서부터 찾아 하나 제거
print(f"remove 후: {fruits}")

for fruit in fruits:                    # L03에서 배운 for 반복문 - 리스트는 이렇게 처음부터 끝까지 훑을 수 있음
    print(f"- {fruit}")

print(f"'apple'이 리스트에 있나요? {'apple' in fruits}")   # in - 값이 리스트 안에 있는지 확인, 결과는 True/False