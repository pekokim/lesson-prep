import functools
from app.logger import get_logger

logger = get_logger(__name__)   # 이 파일(decorators) 이름으로 된 로거 하나를 생성


def log_call(func):
    # log_call(func) - 함수 func를 감싸서, 호출 시작/종료를 자동으로 로그로 남기는 새 함수를 만들어 반환
    @functools.wraps(func)   # wraps(func) - wrapper의 이름/설명이 원래 func처럼 보이도록 정보를 복사
    def wrapper(*args, **kwargs):   # *args, **kwargs - func가 어떤 인자를 받든 그대로 전달할 수 있게 함
        logger.info(f"{func.__name__} 호출 시작 (args={args}, kwargs={kwargs})")
        result = func(*args, **kwargs)   # 원래 함수를 실제로 실행
        logger.info(f"{func.__name__} 호출 종료 (반환값={result})")
        return result
    return wrapper