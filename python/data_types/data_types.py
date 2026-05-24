# =============================================================
# 자료형 (Data Types)
# =============================================================

# =============================================================
# 1. 숫자형 (Numeric Types)
# =============================================================
int_num = 42            # 정수 (int)
float_num = 3.14        # 실수 (float)
neg_num = -10           # 음수도 가능

# 사칙연산
print(10 + 3)           # 13  (덧셈)
print(10 - 3)           # 7   (뺄셈)
print(10 * 3)           # 30  (곱셈)
print(10 / 3)           # 3.333... (나눗셈 → 항상 float)
print(10 // 3)          # 3   (몫, 정수 나눗셈)
print(10 % 3)           # 1   (나머지)
print(2 ** 8)           # 256 (거듭제곱)

# =============================================================
# 2. 문자열 (String)
# =============================================================
greeting = "Hello, World!"
name = 'Python'         # 작은따옴표도 동일

# 문자열 연결
print("Hello" + " " + "Python")    # Hello Python

# 문자열 반복
print("ha" * 3)                     # hahaha

# 문자열 길이
print(len(greeting))                # 13

# 인덱싱 (0번부터 시작)
print(greeting[0])                  # H
print(greeting[-1])                 # !  (뒤에서 첫 번째)

# 슬라이싱 [시작:끝] (끝 인덱스는 포함하지 않음)
print(greeting[0:5])                # Hello
print(greeting[7:])                 # World!

# 문자열 메서드
sentence = "  hello python  "
print(sentence.strip())             # "hello python"  (앞뒤 공백 제거)
print(sentence.upper())             # "  HELLO PYTHON  "
print(sentence.lower())             # "  hello python  "
print("hello".replace("l", "r"))   # "herro"
print("a,b,c".split(","))          # ['a', 'b', 'c']

# f-string (변수를 문자열 안에 넣기)
age = 20
print(f"나이: {age}세")             # 나이: 20세
print(f"내년엔 {age + 1}세")        # 내년엔 21세

# =============================================================
# 3. 리스트 (List) — 순서 있음, 변경 가능
# =============================================================
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]       # 다른 타입 섞기 가능

print(fruits[0])                    # apple
print(fruits[-1])                   # cherry

fruits.append("mango")             # 맨 뒤에 추가
fruits.insert(1, "grape")          # 인덱스 1에 삽입
fruits.remove("banana")            # 값으로 삭제
popped = fruits.pop()              # 맨 뒤 요소 꺼내기
print(fruits)
print(len(fruits))                  # 리스트 길이

# =============================================================
# 4. 튜플 (Tuple) — 순서 있음, 변경 불가
# =============================================================
coordinates = (37.5, 127.0)        # 위도, 경도처럼 바뀌지 않는 값에 사용
rgb = (255, 128, 0)

print(coordinates[0])              # 37.5
# coordinates[0] = 0              # 오류! 튜플은 수정 불가

# =============================================================
# 5. 딕셔너리 (Dictionary) — 키-값 쌍
# =============================================================
person = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

print(person["name"])              # Alice
print(person.get("age"))           # 20 (키가 없어도 오류 없이 None 반환)

person["grade"] = "A"              # 새 키-값 추가
person["age"] = 21                 # 값 수정

print(person.keys())               # dict_keys(['name', 'age', 'major', 'grade'])
print(person.values())             # dict_values([...])
print(person.items())              # 키-값 쌍 목록

# =============================================================
# 6. 집합 (Set) — 중복 없음, 순서 없음
# =============================================================
s = {1, 2, 3, 2, 1}               # 중복 자동 제거
print(s)                           # {1, 2, 3}

s.add(4)
s.remove(2)

a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)                       # {1, 2, 3, 4}  합집합
print(a & b)                       # {2, 3}        교집합
print(a - b)                       # {1}           차집합

# =============================================================
# 7. 불리언 (Boolean)
# =============================================================
t = True
f = False

print(t and f)                     # False (둘 다 True여야 True)
print(t or f)                      # True  (하나라도 True면 True)
print(not t)                       # False (반전)

# 비교 연산의 결과는 항상 bool
print(5 > 3)                       # True
print(5 == 5)                      # True
print(5 != 3)                      # True
