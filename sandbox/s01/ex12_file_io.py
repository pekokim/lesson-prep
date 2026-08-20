# 'w' 모드 - 파일을 새로 쓰기 위해 열기 (이미 있던 내용은 사라지고 새로 씀)
with open("project/sandbox/s01/notes.txt", "w", encoding="utf-8") as f:   # with문 - 블록이 끝나면 파일을 자동으로 닫아줌
    f.write("첫 번째 메모\n")     # write() - 문자열을 파일에 그대로 씀 (줄바꿈은 \n을 직접 넣어야 함)
    f.write("두 번째 메모\n")

# 'a' 모드 - 기존 내용 뒤에 이어서 추가하기 (파일을 새로 덮어쓰지 않음)
with open("project/sandbox/s01/notes.txt", "a", encoding="utf-8") as f:
    f.write("세 번째 메모(추가됨)\n")

# 'r' 모드 - 읽기 전용으로 파일 열기
with open("project/sandbox/s01/notes.txt", "r", encoding="utf-8") as f:
    content = f.read()          # read() - 파일 전체 내용을 하나의 문자열로 읽음

print(f"read()로 읽은 전체 내용:\n{content}")
print(f"글자 수: {len(content)}자")   # 줄바꿈(\n)도 한 글자로 세어짐
