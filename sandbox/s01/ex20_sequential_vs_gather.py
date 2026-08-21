import asyncio   # asyncio - 파이썬에서 비동기 처리를 담당하는 표준 모듈
import time      # time - 걸린 시간을 재기 위해 사용


async def download_file(name, seconds):   # name: 화면에 표시할 작업 이름 / seconds: 걸리는 시간(초)
    print(f"{name} 다운로드 시작")
    await asyncio.sleep(seconds)   # 실제 네트워크 다운로드 대기를 흉내 (진짜로 기다리는 대신 자리를 양보함)
    print(f"{name} 다운로드 완료")
    return name


async def run_sequential():
    start = time.perf_counter()                        # perf_counter() - 정밀한 경과 시간 측정용 시계
    for name in ["파일A", "파일B", "파일C", "파일D"]:     # 작업 4개를 하나씩 순서대로 처리
        await download_file(name, 1)                    # 하나가 끝나야 다음 줄로 넘어감 (순차)
    return time.perf_counter() - start                  # 총 걸린 시간을 돌려줌


async def run_concurrent():
    start = time.perf_counter()
    results = await asyncio.gather(       # gather - 아래 4개를 한꺼번에 넘겨 동시에 처리시킴
        download_file("파일A", 1),
        download_file("파일B", 1),
        download_file("파일C", 1),
        download_file("파일D", 1),
    )
    print(f"동시 실행 결과:{results}")     # 결과는 넘긴 순서 그대로 list로 돌아옴
    return time.perf_counter() - start


async def main():
    print("=== 1) 순차 실행: await로 하나씩 ===")
    sequential_elapsed = await run_sequential()
    print("=== 2) 동시 실행: asyncio.gather로 한꺼번에 ===")
    concurrent_elapsed = await run_concurrent()
    print(f"[비교] 순차 실행{sequential_elapsed:.1f}초 vs 동시 실행{concurrent_elapsed:.1f}초")

asyncio.run(main())   # 프로그램 시작점 - 이 한 줄이 있어야 위 코루틴들이 실제로 실행됨