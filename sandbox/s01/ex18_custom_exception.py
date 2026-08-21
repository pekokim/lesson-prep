class InsufficientFundsError(Exception):   # Exception을 상속받아 새로운 종류의 예외를 정의
    """계좌 잔액이 부족할 때 발생시키는 커스텀 예외."""

    def __init__(self, balance, amount):
        self.balance = balance                # 어떤 상황이었는지 알 수 있도록 관련 값들을 저장
        self.amount = amount
        message = f"잔액 부족: 현재{balance}원, 요청 금액{amount}원"
        super().__init__(message)             # 부모(Exception)의 __init__을 호출해 에러 메시지를 등록


def withdraw(balance, amount):
    # 인출하려는 금액이 잔액보다 크면 직접 예외를 발생시킴
    if amount > balance:
        raise InsufficientFundsError(balance, amount)   # raise - 커스텀 예외를 직접 발생시킴
    return balance - amount


print(f"정상 인출:{withdraw(10000, 3000)}원 남음")

try:
    withdraw(10000, 15000)         # 잔액보다 큰 금액을 인출 시도 -> InsufficientFundsError 발생
except InsufficientFundsError as error:
    print(f"인출 실패:{error}")
    print(f"에러에 담긴 정보 - 잔액:{error.balance}, 요청 금액:{error.amount}")