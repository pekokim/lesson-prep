import logging

# basicConfig - 프로그램 전체에서 공통으로 쓸 로그 형식을 딱 한 번만 설정
logging.basicConfig(
    level=logging.INFO,   # INFO 이상 레벨(INFO,WARNING, ERROR, CRITICAL)만 화면에 출력, DEBUG는 숨김
    format="%(asctime)s [%(levelname)s]%(name)s:%(message)s",   # 시간, 레벨, 로거 이름, 메시지 순으로 출력
    datefmt="%H:%M:%S",
)


def get_logger(name):
    # 모듈마다 이 함수로 로거를 하나씩 받아서 사용 (보통 get_logger(__name__)으로 호출)
    return logging.getLogger(name)