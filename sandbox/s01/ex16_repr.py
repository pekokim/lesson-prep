class PlainDog:                          # __repr__을 정의하지 않은 클래스
    def __init__(self, name):
        self.name = name


class ReprDog:                           # __repr__을 정의한 클래스
    def __init__(self, name):
        self.name = name

    def __repr__(self):                   # __repr__ - 이 객체를 print()하거나 화면에 표시할 때 쓸 문자열을 정함
        return f"ReprDog(name={self.name!r})"


plain = PlainDog("초코")
nice = ReprDog("초코")

print(f"__repr__ 없는 경우: {plain}")     # 기본 표시 방식 - 메모리 주소가 섞인 알아보기 힘든 문자열
print(f"__repr__ 있는 경우: {nice}")      # __repr__에서 정한 문자열이 그대로 출력됨

print(f"리스트 안에 있을 때도 동일하게 적용: {[nice, nice]}")   # list 안의 객체를 출력할 때도 __repr__이 쓰임
