import asyncio
import time
from app.documents import SAMPLE_DOCUMENTS
from app.logger import get_logger

logger = get_logger(__name__)


async def fetch_embedding(document):
    # async def - 이 함수는 "코루틴(Coroutine)"을 만드는 함수이며, 호출만 해서는 실행되지 않고 await해야 실행됨
    logger.info(f"{document.title} 임베딩 요청 시작")
    await asyncio.sleep(1)   # 실제로는 임베딩 API를 호출하지만, 지금은 네트워크 대기(1초)를 흉내만 냄
    logger.info(f"{document.title} 임베딩 요청 완료")
    return {"doc_id": document.id, "embedding_preview": f"vector_for_doc_{document.id}"}


async def fetch_embeddings_sequential(documents):
    # 순차 처리 - 문서 하나의 임베딩이 끝나야 다음 문서로 넘어감 (await가 끝날 때까지 기다림)
    results = []
    for doc in documents:
        result = await fetch_embedding(doc)   # await - 이 코루틴이 끝날 때까지 여기서 기다림
        results.append(result)
    return results


async def fetch_embeddings_concurrent(documents):
    # 동시 처리 - 코루틴들을 먼저 다 만들어두고, asyncio.gather로 한꺼번에 실행해서 기다림
    tasks = []
    for doc in documents:
        tasks.append(fetch_embedding(doc))   # 호출만 하면 아직 실행 안 된 코루틴 객체가 생성됨
    results = await asyncio.gather(*tasks)    # gather(*tasks) - 여러 코루틴을 동시에 실행하고 모두 끝나길 기다림
    return results


async def main():
    print(f"[임베딩 확인] 대상 문서 수:{len(SAMPLE_DOCUMENTS)}건")

    start = time.perf_counter()                                   # perf_counter() - 정밀한 경과 시간 측정용
    sequential_results = await fetch_embeddings_sequential(SAMPLE_DOCUMENTS)
    sequential_elapsed = time.perf_counter() - start
    print(f"[순차 처리] 결과 수:{len(sequential_results)}건, 걸린 시간:{sequential_elapsed:.1f}초")

    start = time.perf_counter()
    concurrent_results = await fetch_embeddings_concurrent(SAMPLE_DOCUMENTS)
    concurrent_elapsed = time.perf_counter() - start
    print(f"[동시 처리] 결과 수:{len(concurrent_results)}건, 걸린 시간:{concurrent_elapsed:.1f}초")


if __name__ == "__main__":
    asyncio.run(main())   # asyncio.run() - 프로그램 진입점에서 최상위 코루틴을 실행하는 표준 방법