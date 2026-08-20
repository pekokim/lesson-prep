user = {"name": "김민준", "age": 25, "is_student": True}   # dict - key: value 쌍으로 값을 저장 ({}로 만듦)
print(f"전체 딕셔너리: {user}")

print(f"이름 조회(user['name']): {user['name']}")   # [] - key로 값을 바로 조회 (없는 key면 에러가 남)
print(f"전화번호 조회(get): {user.get('phone', '등록된 번호 없음')}")   # get(key, 기본값) - key가 없어도 에러 없이 기본값을 돌려줌

user["age"] = 26                       # 이미 있는 key에 값을 대입하면 -> 수정
print(f"age 수정 후: {user}")

user["email"] = "minjun@example.com"   # 없던 key에 값을 대입하면 -> 새 항목 추가
print(f"email 추가 후: {user}")

print(f"'name' key가 있나요? {'name' in user}")   # in - key가 있는지 확인 (list와 달리 '값'이 아니라 'key'를 봄)

del user["is_student"]                 # del - key를 지정해 항목 제거
print(f"is_student 삭제 후: {user}")

print(f"모든 key: {list(user.keys())}")       # keys() - key만 모아서 확인 (list()로 감싸면 보기 좋게 출력됨)
print(f"모든 value: {list(user.values())}")   # values() - value만 모아서 확인