# =============================================================
# OOP 기초 (Object-Oriented Programming)
# =============================================================
# 객체 지향 프로그래밍은 데이터(속성)와 기능(메서드)을
# 하나의 클래스로 묶어서 관리하는 방식입니다.
#
# 클래스(Class) : 객체를 만드는 설계도
# 객체(Object)  : 클래스로 만들어진 실체 (인스턴스)
# 속성(Attribute): 객체가 가진 데이터 (변수)
# 메서드(Method) : 객체가 할 수 있는 동작 (함수)

# =============================================================
# 1. 클래스 정의와 객체 생성
# =============================================================
class Dog:
    # __init__ : 객체가 생성될 때 자동으로 호출되는 초기화 메서드
    # self      : 객체 자신을 가리키는 매개변수 (항상 첫 번째로 작성)
    def __init__(self, name, breed, age):
        self.name = name        # 인스턴스 속성
        self.breed = breed
        self.age = age

    # 메서드 정의
    def bark(self):
        print(f"{self.name}: 왈왈!")

    def info(self):
        print(f"이름: {self.name}, 품종: {self.breed}, 나이: {self.age}살")


# 객체(인스턴스) 생성 — 클래스이름(인수)
dog1 = Dog("초코", "말티즈", 3)
dog2 = Dog("바둑이", "진돗개", 5)

# 속성 접근
print(dog1.name)        # 초코
print(dog2.age)         # 5

# 메서드 호출
dog1.bark()             # 초코: 왈왈!
dog2.info()             # 이름: 바둑이, 품종: 진돗개, 나이: 5살

# 각 객체는 서로 독립적
dog1.name = "흰둥이"    # dog1의 속성만 변경
print(dog1.name)        # 흰둥이
print(dog2.name)        # 바둑이 (영향 없음)

# =============================================================
# 2. 클래스 변수 vs 인스턴스 변수
# =============================================================
class Student:
    school = "YJU"          # 클래스 변수 — 모든 객체가 공유

    def __init__(self, name, grade):
        self.name = name    # 인스턴스 변수 — 객체마다 따로 보유
        self.grade = grade

    def introduce(self):
        print(f"[{self.school}] {self.name} ({self.grade}학년)")


s1 = Student("Alice", 2)
s2 = Student("Bob", 3)

s1.introduce()          # [YJU] Alice (2학년)
s2.introduce()          # [YJU] Bob (3학년)

# 클래스 변수는 클래스 이름으로 접근 가능
print(Student.school)   # YJU

# 클래스 변수를 바꾸면 모든 객체에 반영
Student.school = "한국대학교"
s1.introduce()          # [한국대학교] Alice (2학년)
s2.introduce()          # [한국대학교] Bob (3학년)

# =============================================================
# 3. 다양한 메서드 종류
# =============================================================
class Circle:
    PI = 3.14159            # 클래스 변수

    def __init__(self, radius):
        self.radius = radius

    # 인스턴스 메서드 — self를 통해 인스턴스 속성에 접근
    def area(self):
        return self.PI * self.radius ** 2

    def perimeter(self):
        return 2 * self.PI * self.radius

    # 클래스 메서드 — cls를 통해 클래스 자체에 접근
    @classmethod
    def from_diameter(cls, diameter):   # 지름으로 객체 생성하는 대안 생성자
        return cls(diameter / 2)

    # 정적 메서드 — self/cls 없이 독립적으로 동작하는 유틸리티 함수
    @staticmethod
    def is_valid_radius(r):
        return r > 0

    # __str__ — print()할 때 보여줄 문자열 정의
    def __str__(self):
        return f"Circle(반지름={self.radius})"


c1 = Circle(5)
print(c1.area())                    # 78.53975
print(c1.perimeter())               # 31.4159
print(c1)                           # Circle(반지름=5)  ← __str__ 호출

c2 = Circle.from_diameter(10)      # 클래스 메서드로 생성
print(c2.radius)                    # 5.0

print(Circle.is_valid_radius(3))    # True
print(Circle.is_valid_radius(-1))   # False

# =============================================================
# 4. 상속 (Inheritance)
# =============================================================
# 부모 클래스의 속성과 메서드를 자식 클래스가 물려받습니다.

class Animal:                       # 부모(기반) 클래스
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name}: {self.sound}")

    def info(self):
        print(f"동물 이름: {self.name}")


class Cat(Animal):                  # Animal을 상속받은 자식 클래스
    def __init__(self, name, indoor):
        super().__init__(name, "야옹")  # 부모의 __init__ 호출
        self.indoor = indoor            # 자식만의 추가 속성

    def is_indoor(self):
        status = "실내" if self.indoor else "실외"
        print(f"{self.name}은 {status} 고양이입니다")


class Parrot(Animal):
    def __init__(self, name, vocabulary):
        super().__init__(name, "꽥꽥")
        self.vocabulary = vocabulary

    # 메서드 오버라이딩 — 부모 메서드를 재정의
    def speak(self):
        words = ", ".join(self.vocabulary)
        print(f"{self.name}: {words}")


cat = Cat("나비", indoor=True)
parrot = Parrot("폴리", ["안녕", "맛있다", "배고파"])

cat.speak()             # 나비: 야옹
cat.info()              # 동물 이름: 나비  (부모 메서드 그대로 사용)
cat.is_indoor()         # 나비은 실내 고양이입니다

parrot.speak()          # 폴리: 안녕, 맛있다, 배고파  (오버라이딩된 메서드)
parrot.info()           # 동물 이름: 폴리

# 상속 확인
print(isinstance(cat, Cat))         # True
print(isinstance(cat, Animal))      # True  (부모 타입도 True)
print(isinstance(cat, Parrot))      # False

# =============================================================
# 5. 캡슐화 (Encapsulation) — 속성 보호
# =============================================================
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance    # __ 접두사 → 외부에서 직접 접근 불가 (private)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount}원 입금 완료. 잔액: {self.__balance}원")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("잔액 부족")
        else:
            self.__balance -= amount
            print(f"{amount}원 출금 완료. 잔액: {self.__balance}원")

    # 잔액은 읽기만 허용 (getter)
    def get_balance(self):
        return self.__balance


account = BankAccount("Alice", 10000)
account.deposit(5000)               # 5000원 입금 완료. 잔액: 15000원
account.withdraw(3000)              # 3000원 출금 완료. 잔액: 12000원
account.withdraw(20000)             # 잔액 부족
print(account.get_balance())        # 12000

# print(account.__balance)          # 오류! 외부에서 직접 접근 불가

# =============================================================
# 6. 매직 메서드 (Magic Methods / Dunder Methods)
# =============================================================
# __로 시작하고 끝나는 특별한 메서드로, Python 내장 연산자와 연동됩니다.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):              # print() 호출 시
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):             # 개발자용 문자열 표현
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):       # + 연산자
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):              # len() 호출 시
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __eq__(self, other):        # == 연산자
        return self.x == other.x and self.y == other.y


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1)                           # Vector(1, 2)
print(v1 + v2)                      # Vector(4, 6)
print(len(v2))                      # 5  (3-4-5 직각삼각형)
print(v1 == Vector(1, 2))           # True
print(v1 == v2)                     # False
