import json          # json 모듈 - list/dict를 그대로 파일로 저장하고 다시 읽어올 수 있게 해주는 표준 모듈
import os            # os 모듈 - 파일이 실제로 존재하는지 확인할 때 사용
from app.documents import SAMPLE_DOCUMENTS   # 파일이 없을 때 사용할 기본 문서 목록


def save_documents(documents, filepath):
    # 문서 list를 JSON 형식으로 파일에 저장 (encoding='utf-8' - 한글이 깨지지 않도록 반드시 지정)
    with open(filepath, "w", encoding="utf-8") as f:   # with문 - 저장이 끝나면 파일을 자동으로 닫아줌
        json.dump(documents, f, ensure_ascii=False, indent=2)   # ensure_ascii=False - 한글을 유니코드 코드로 안 바꾸고 그대로 저장


def load_documents(filepath):
    # 파일이 있으면 그 내용을 읽어 list로 반환하고, 없으면 SAMPLE_DOCUMENTS를 기본값으로 반환
    if not os.path.exists(filepath):   # os.path.exists() - 경로에 파일이 실제로 있는지 확인
        return SAMPLE_DOCUMENTS
    with open(filepath, "r", encoding="utf-8") as f:   # 'r' 모드 - 읽기 전용으로 파일 열기
        return json.load(f)             # json.load() - 파일 내용을 파싱해서 파이썬 list/dict로 되돌림


if __name__ == "__main__":
    data_path = "data/documents.json"   # project/ 폴더 기준 상대 경로

    print(f"[저장소 확인] 저장 전 파일 존재 여부: {os.path.exists(data_path)}")

    save_documents(SAMPLE_DOCUMENTS, data_path)   # 샘플 문서를 파일로 저장
    print(f"[저장소 확인] 저장 후 파일 존재 여부: {os.path.exists(data_path)}")

    loaded = load_documents(data_path)             # 방금 저장한 파일을 다시 읽어옴
    print(f"[저장소 확인] 불러온 문서 수: {len(loaded)}건")
    print(f"[저장소 확인] 첫 번째 문서 제목: {loaded[0]['title']}")
    print(f"[저장소 확인] 원본과 동일한가?: {loaded == SAMPLE_DOCUMENTS}")   # 저장 전/후 데이터가 같은지 비교
    