import functools
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s]%(message)s")   # 로그 출력 형식을 한 번만 설정
logger = logging.getLogger(__name__)


def log_call(func):                    # 데코레이터 - 함수를 인자로 받아, 새로운 함수(wrapper)를 반환하는 함수
    @functools.wraps(func)              # wraps(func) - wrapper가 원래 func의 이름 등 정보를 그대로 갖도록 함
    def wrapper(*args, **kwargs):        # *args, **kwargs - 원래 함수가 어떤 인자를 받든 그대로 대신 받아줌
        logger.info(f"{func.__name__} 시작")
        result = func(*args, **kwargs)   # 진짜 함수(func)를 이 시점에 실행
        logger.info(f"{func.__name__} 종료, 결과={result}")
        return result
    return wrapper


@log_call                # @log_call - "add = log_call(add)"와 완전히 같은 뜻
def add(a, b):
    return a + b


print(f"__name__ 확인(wraps 덕분에 원래 이름 유지):{add.__name__}")   # wraps가 없었다면 "wrapper"로 나왔을 것
result = add(3, 4)
print(f"add(3, 4) 결과:{result}")