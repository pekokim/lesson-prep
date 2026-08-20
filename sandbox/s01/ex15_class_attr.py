class Dog:
    species = "Canis familiaris"    # 클래스 속성 - class 블록 바로 아래에 두면 모든 인스턴스가 공유하는 값
    total_count = 0                  # 클래스 속성 - 지금까지 만들어진 Dog 인스턴스 수를 세는 용도

    def __init__(self, name, age):
        self.name = name              # 인스턴스 속성 - 각 인스턴스마다 따로 저장됨
        self.age = age
        Dog.total_count += 1          # 클래스 이름으로 클래스 속성에 접근해 값을 1 증가 (모든 인스턴스가 공유)


dog1 = Dog("초코", 3)
dog2 = Dog("나비", 5)

print(f"dog1.species: {dog1.species}")   # 인스턴스에서도 클래스 속성을 그대로 읽을 수 있음
print(f"dog2.species: {dog2.species}")
print(f"Dog.species: {Dog.species}")      # 클래스 자체에서도 바로 읽을 수 있음

print(f"현재까지 만들어진 Dog 수: {Dog.total_count}마리")   # 인스턴스가 아니라 클래스 자체가 이 값을 갖고 있음

dog1.name = "초코(수정됨)"                # 인스턴스 속성은 각자 독립적이라, dog1만 바꿔도 dog2는 영향받지 않음
print(f"dog1.name 변경 후 -> dog1: {dog1.name}, dog2: {dog2.name}")
