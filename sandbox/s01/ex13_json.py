import json   # json 모듈 - 파이썬 list/dict를 파일에 저장하고 다시 되돌려주는 표준 모듈

tasks = [
    {"title": "보고서 작성", "done": False},
    {"title": "회의 준비", "done": True},
]

with open("project/sandbox/s01/tasks.json", "w", encoding="utf-8") as f:
    # dump(저장할 데이터, 파일객체, ...) - 데이터를 JSON 형식으로 바꿔 파일에 바로 씀
    # ensure_ascii=False - 한글을 \uXXXX 코드로 바꾸지 않고 사람이 읽을 수 있는 그대로 저장
    # indent=2 - 두 칸씩 들여써서 사람이 눈으로 확인하기 좋게 저장 (없으면 한 줄로 붙어서 저장됨)
    json.dump(tasks, f, ensure_ascii=False, indent=2)

with open("project/sandbox/s01/tasks.json", "r", encoding="utf-8") as f:
    loaded_tasks = json.load(f)   # load(파일객체) - 파일에 저장된 JSON을 읽어 파이썬 list/dict로 되돌림

print(f"파일에서 다시 불러온 값: {loaded_tasks}")
print(f"원본과 동일한가?: {tasks == loaded_tasks}")   # 저장 전/후 값이 같은지 비교
print(f"불러온 값의 타입: {type(loaded_tasks)}, 첫 번째 항목의 타입: {type(loaded_tasks[0])}")
