import asyncio


async def greet(name):           # async def - 이 함수를 호출하면 "코루틴 객체(주문서)"가 만들어짐
    await asyncio.sleep(1)        # await - 1초 기다리는 동안 주방장에게 자리를 양보
    return f"안녕하세요,{name}님!"


result_without_await = greet("Arim")   # await 없이 호출 - 주문서만 쓰고 주방에 넘기지 않은 상태
print(f"await 없이 호출한 결과:{result_without_await}")
print(f"타입 확인:{type(result_without_await)}")


async def main():
    result = await greet("Arim")   # await를 붙여야 실제로 실행되고, 끝난 뒤 결과를 돌려받음
    print(f"await로 실행한 결과:{result}")


asyncio.run(main())   # 주방 문 열기 - 이 줄이 있어야 위 코루틴이 실제로 처리됨