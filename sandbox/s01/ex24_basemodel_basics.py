from pydantic import BaseModel   # BaseModel - 이 클래스를 상속하면 필드 타입을 선언하는 것만으로 자동 검증이 생김


class User(BaseModel):           # class 문법은 L01(클래스)과 완전히 동일, 다른 점은 BaseModel을 상속한다는 것
    name: str                     # 타입 힌트(: str)가 "이 필드는 반드시 이 타입이어야 한다"는 검증 규칙이 됨
    age: int
    is_active: bool = True        # 기본값을 지정하면 "필수는 아니고, 안 주면 이 값을 쓴다"는 뜻


user1 = User(name="김민준", age=25)              # is_active를 안 줬으므로 기본값 True가 자동으로 채워짐
print(f"user1:{user1}")
print(f"user1.age의 타입:{type(user1.age)}")

user2 = User(name="이서연", age="30")             # age에 문자열 "30"을 넣었지만...
print(f"user2:{user2}")
print(f"user2.age의 타입:{type(user2.age)}")     # Pydantic이 자동으로 int로 변환해줌 (타입 강제 변환)

print(f"model_dump()로 dict 변환:{user1.model_dump()}")   # model_dump() - 인스턴스를 dict로 변환 (L01의 to_dict()와 같은 역할)