point = (3, 5)                          # tuple - list와 비슷하지만 ()로 만들고, 한 번 만들면 값을 바꿀 수 없음
print(f"좌표 튜플: {point}, x={point[0]}, y={point[1]}")   # 값을 꺼내 쓰는 방법(인덱싱)은 list와 완전히 동일

sizes = {"S", "M", "L", "M", "S"}       # set - 같은 값을 여러 번 넣어도 한 번만 남는 자료구조({}로 만듦)
print(f"중복 제거된 set: {sizes}")
print(f"몇 종류인가요? {len(sizes)}")
print(f"'XL' 사이즈가 있나요? {'XL' in sizes}")   # in - set에서 '이 값이 있는지' 확인하는 가장 흔한 사용법

# 여기서부터는 오늘 프로젝트에서 그대로 쓰는 모양입니다: 여러 건이니까 list, 한 건은 여러 정보를 담으니까 dict
cart_items = [
    {"name": "keyboard", "price": 35000},
    {"name": "mouse", "price": 15000},
]
total = 0                                # 합계를 담을 변수를 0으로 시작 (누적할 그릇)
for item in cart_items:                  # list를 훑으면 item에는 dict가 하나씩 들어옴
    print(f"- {item['name']}: {item['price']}원")   # dict에서 key로 값을 꺼내 출력
    total = total + item["price"]        # 꺼낸 가격을 기존 합계에 더해 다시 total에 저장
print(f"총 금액: {total}원")