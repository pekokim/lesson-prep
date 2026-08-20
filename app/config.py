PROJECT_NAME = "Enterprise AI Office Assistant"
PROJECT_VERSION = "0.1.0"

IS_DEBUG = True

DOCUMENT_DOMAIN = "Company Policy Documents"

MAX_UPLOAD_SIZE_MB = 10          
BYTES_PER_MB = 1024 * 1024       
MAX_UPLOAD_SIZE_BYTES = MAX_UPLOAD_SIZE_MB * BYTES_PER_MB 

MIN_DOCUMENT_LENGTH = 10  

IS_VALID_MAX_SIZE = MAX_UPLOAD_SIZE_MB > 0   

if __name__ == "__main__":
    print(f"[설정 확인] 업로드 용량 설정이 유효한가?: {IS_VALID_MAX_SIZE}")
    print(f"[설정 확인] 프로젝트: {PROJECT_NAME} (v{PROJECT_VERSION})")
    print(f"[설정 확인] 디버그 모드: {IS_DEBUG} (타입: {type(IS_DEBUG)})")
    print(f"[설정 확인] 문서 도메인: {DOCUMENT_DOMAIN}")
    print(f"[설정 확인] 최대 업로드 용량: {MAX_UPLOAD_SIZE_MB}MB = {MAX_UPLOAD_SIZE_BYTES}바이트")
    print(f"[설정 확인] 최소 문서 길이: {MIN_DOCUMENT_LENGTH}자 이상")
