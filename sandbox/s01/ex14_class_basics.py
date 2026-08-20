class Dog:                              # class - 새로운 "틀(설계도)"을 만드는 문법, 이름은 관례상 대문자로 시작
    def __init__(self, name, age):       # __init__ - Dog(...)를 호출하는 순간 자동으로 실행되는 메서드
        self.name = name                 # self.name = name -> 이 인스턴스만의 이름을 저장
        self.age = age                   # self.age = age -> 이 인스턴스만의 나이를 저장

    def bark(self):                      # 메서드 - 클래스 안에 정의된 함수, 첫 매개변수는 항상 self
        return f"{self.name}이(가) 멍멍 짖습니다!"   # self로 자기 자신의 속성에 접근

    def have_birthday(self):
        self.age += 1                    # 메서드 안에서 self.age를 직접 수정 -> 이 인스턴스의 상태가 바뀜
        return f"{self.name}의 나이가 {self.age}살이 되었습니다."


dog1 = Dog("초코", 3)                    # Dog 클래스로 인스턴스(실제 객체) 하나를 생성
dog2 = Dog("나비", 5)                    # 같은 클래스로 또 다른 인스턴스를 생성 (서로 독립적인 값을 가짐)

print(f"dog1: 이름={dog1.name}, 나이={dog1.age}")
print(f"dog2: 이름={dog2.name}, 나이={dog2.age}")

print(dog1.bark())                       # 인스턴스.메서드() 형태로 호출
print(dog2.bark())

print(dog1.have_birthday())
print(f"dog1의 나이만 바뀌었는지 확인 -> dog1: {dog1.age}살, dog2: {dog2.age}살")
