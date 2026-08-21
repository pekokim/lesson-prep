from pydantic import BaseModel, ValidationError   # BaseModel - 타입 힌트를 검사 규칙으로 승격시켜주는 부모 클래스


class Greeting(BaseModel):   # 방금 greet() 함수에 적었던 것과 똑같은 메모(name: str)를 이번엔 Pydantic에게 맡김
    name: str


print(Greeting(name="김민준"))   # 메모대로 문자열 -> 통과
try:
    Greeting(name=123)            # 아까는 그냥 통과했던 정수 123을 다시 넣어보면?
except ValidationError as error:
    print(f"검증 실패:{error.errors()[0]['msg']}")