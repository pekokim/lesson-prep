from pydantic import BaseModel, Field, ValidationError


class Product(BaseModel):
    name: str = Field(min_length=1, max_length=50)        # 문자열 길이 제약 - 1자 이상 50자 이하
    price: int = Field(gt=0)                                # gt=0 - 0보다 커야 함(0 이하는 거부)
    quantity: int = Field(ge=0, default=0)                  # ge=0 - 0 이상, 기본값은 0


product = Product(name="키보드", price=35000, quantity=2)
print(f"정상 생성:{product}")

try:
    Product(name="", price=35000)             # name이 빈 문자열 -> min_length=1 위반
except ValidationError as error:
    print(f"검증 실패(빈 이름):{error.errors()[0]['msg']}")

try:
    Product(name="마우스", price=-1000)        # price가 음수 -> gt=0 위반
except ValidationError as error:
    print(f"검증 실패(음수 가격):{error.errors()[0]['msg']}")

print(f"model_dump()로 dict 변환:{product.model_dump()}")