# [A] 메모리에만 담아두는 방식 - 지금까지 우리가 해온 방식입니다
memos = []                              # 빈 리스트를 만들어 메모를 담을 준비
memos.append("첫 번째 메모")             # 메모를 하나 추가
print(f"[메모리] 현재 메모 수: {len(memos)}건")

# [B] 파일에 남기는 방식 - 오늘 배울 방식입니다 (지금은 따라만 쳐보세요)
with open("project/sandbox/so1/memo.txt", "a", encoding="utf-8") as f:   # "a" = 뒤에 이어서 쓰기 모드
    f.write("메모 한 줄\n")                                   # 파일에 한 줄 추가

with open("project/sandbox/so1/memo.txt", "r", encoding="utf-8") as f:   # "r" = 읽기 전용 모드
    print(f"[파일] 지금까지 쌓인 내용:\n{f.read()}")           # 파일 전체 내용을 출력