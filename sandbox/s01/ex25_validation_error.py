from pydantic import BaseModel, ValidationError   # ValidationError - 검증에 실패하면 발생하는 예외


class User(BaseModel):
    name: str
    age: int
    is_active: bool = True


try:
    User(name="박지훈", age="스물다섯")   # "스물다섯"은 정수로 변환할 수 없는 문자열 -> 검증 실패
except ValidationError as error:
    print(f"에러 발생! 문제가 된 필드 수:{error.error_count()}개")
    for e in error.errors():             # errors() - 어떤 필드가 왜 문제였는지 하나씩 담긴 list를 반환
        print(f"  - 필드:{e['loc']}, 이유:{e['msg']}")

try:
    User(age=25)                          # name을 아예 안 줌 -> 필수 필드 누락으로 검증 실패
except ValidationError as error:
    print(f"에러 발생! 문제가 된 필드 수:{error.error_count()}개")
    for e in error.errors():
        print(f"  - 필드:{e['loc']}, 이유:{e['msg']}")