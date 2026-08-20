import json          # json 모듈 - list/dict를 그대로 파일로 저장하고 다시 읽어올 수 있게 해주는 표준 모듈
import os            # os 모듈 - 파일이 실제로 존재하는지 확인할 때 사용
from app.documents import SAMPLE_DOCUMENTS   # 파일이 없을 때 사용할 기본 문서 목록
from app.models import Document


def save_documents(documents, filepath):
    # Document 인스턴스들을 to_dict()로 dict로 바꾼 뒤 JSON으로 저장 (JSON은 클래스 인스턴스를 직접 저장할 수 없음)
    data = []
    for doc in documents:
        data.append(doc.to_dict())
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_documents(filepath):
    # 파일이 있으면 dict 목록을 읽어 각각 Document로 되살리고, 없으면 SAMPLE_DOCUMENTS를 기본값으로 반환
    if not os.path.exists(filepath):
        return SAMPLE_DOCUMENTS
    with open(filepath, "r", encoding="utf-8") as f:
        raw_list = json.load(f)   # 이 시점의 raw_list는 아직 dict들의 list (Document 인스턴스가 아님)

    documents = []
    for item in raw_list:
        documents.append(Document(item["id"], item["title"], item["content"], item["category"]))
    return documents


if __name__ == "__main__":
    data_path = "data/documents.json"

    print(f"[저장소 확인] 저장 전 파일 존재 여부: {os.path.exists(data_path)}")

    save_documents(SAMPLE_DOCUMENTS, data_path)
    print(f"[저장소 확인] 저장 후 파일 존재 여부: {os.path.exists(data_path)}")

    loaded = load_documents(data_path)
    print(f"[저장소 확인] 불러온 문서 수: {len(loaded)}건")
    print(f"[저장소 확인] 첫 번째 문서: {loaded[0]}")                       # Document.__repr__로 출력됨
    print(f"[저장소 확인] 첫 번째 문서가 Document 인스턴스인가?: {isinstance(loaded[0], Document)}")