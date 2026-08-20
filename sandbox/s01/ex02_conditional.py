score = 82   # 판정할 점수 - 정수

if score >= 90:           # 조건1: 90점 이상인가
    grade = "A"
elif score >= 80:          # 조건1이 거짓일 때만 확인하는 조건2: 80점 이상인가
    grade = "B"
elif score >= 70:          # 조건1, 조건2 모두 거짓일 때만 확인하는 조건3
    grade = "C"
else:                       # 앞의 모든 조건이 거짓일 때
    grade = "D"

print(f"점수 {score}점의 등급: {grade}")

# 조건식에는 지난 차시에서 배운 논리 연산자(or)를 그대로 이어 붙일 수 있음
# "A이거나 B이거나 C이면 통과" -> or로 세 조건을 연결하면 셋 중 하나만 참이어도 전체가 참
if grade == "A" or grade == "B" or grade == "C":
    is_pass = True                # 세 등급 중 하나에 해당하므로 통과
else:
    is_pass = False               # 그 외(D)는 통과하지 못함

print(f"통과 여부: {is_pass}")