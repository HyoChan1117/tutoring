# =============================================================
# 딕셔너리 (Dictionary)
# =============================================================
# 딕셔너리는 키(key)-값(value) 쌍으로 데이터를 저장합니다.
# 중괄호 {}로 만들며, 키로 값을 빠르게 찾을 수 있습니다.
# 키는 중복될 수 없고, 값은 어떤 타입이든 가능합니다.

# =============================================================
# 1. 딕셔너리 만들기
# =============================================================
empty = {}                              # 빈 딕셔너리
empty2 = dict()                         # dict()로도 생성 가능

person = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "is_student": True
}

# dict()로 만들기
config = dict(host="localhost", port=8080, debug=True)

print(person)
print(config)

# =============================================================
# 2. 값 접근
# =============================================================
student = {"name": "Bob", "score": 95, "grade": "A"}

# 키로 직접 접근
print(student["name"])          # Bob
print(student["score"])         # 95
# print(student["phone"])       # 오류! 없는 키 접근 시 KeyError 발생

# get() — 키가 없으면 None 반환 (오류 없음)
print(student.get("grade"))     # A
print(student.get("phone"))     # None
print(student.get("phone", "없음"))  # "없음" (기본값 지정)

# =============================================================
# 3. 값 추가 및 수정
# =============================================================
info = {"name": "Charlie", "age": 22}

info["city"] = "Seoul"          # 새 키-값 추가
print(info)                     # {'name': 'Charlie', 'age': 22, 'city': 'Seoul'}

info["age"] = 23                # 기존 키의 값 수정
print(info)                     # {'name': 'Charlie', 'age': 23, 'city': 'Seoul'}

# update() — 여러 키-값 한 번에 추가/수정
info.update({"major": "Math", "age": 24})
print(info)

# =============================================================
# 4. 값 삭제
# =============================================================
data = {"a": 1, "b": 2, "c": 3, "d": 4}

del data["a"]                   # 키로 삭제
print(data)                     # {'b': 2, 'c': 3, 'd': 4}

removed = data.pop("b")         # 꺼내기 (반환값 있음)
print(removed)                  # 2
print(data)                     # {'c': 3, 'd': 4}

# pop() 기본값 설정 (없는 키도 오류 없이 처리)
val = data.pop("z", "없음")
print(val)                      # 없음

data.clear()                    # 모든 항목 삭제
print(data)                     # {}

# =============================================================
# 5. 키/값/쌍 목록 가져오기
# =============================================================
scores = {"Alice": 90, "Bob": 85, "Charlie": 92}

print(scores.keys())            # dict_keys(['Alice', 'Bob', 'Charlie'])
print(scores.values())          # dict_values([90, 85, 92])
print(scores.items())           # dict_items([('Alice', 90), ...])

# 리스트로 변환
key_list = list(scores.keys())
print(key_list)                 # ['Alice', 'Bob', 'Charlie']

# =============================================================
# 6. 딕셔너리 순회
# =============================================================
grades = {"Alice": "A", "Bob": "B", "Charlie": "A+"}

# 키만 순회 (기본)
for name in grades:
    print(name)

# 키와 값 함께 순회
for name, grade in grades.items():
    print(f"{name}: {grade}")

# 값만 순회
for grade in grades.values():
    print(grade)

# =============================================================
# 7. 키 존재 여부 확인
# =============================================================
config = {"debug": True, "port": 3000}

print("debug" in config)        # True
print("host" in config)         # False
print("host" not in config)     # True

# =============================================================
# 8. 중첩 딕셔너리 (Nested Dictionary)
# =============================================================
students = {
    "s001": {"name": "Alice", "age": 20, "score": 95},
    "s002": {"name": "Bob",   "age": 21, "score": 88},
    "s003": {"name": "Charlie", "age": 19, "score": 92},
}

# 중첩 접근
print(students["s001"]["name"])         # Alice
print(students["s002"]["score"])        # 88

# 중첩 딕셔너리 순회
for sid, info in students.items():
    print(f"학번: {sid}, 이름: {info['name']}, 점수: {info['score']}")

# =============================================================
# 9. 딕셔너리 컴프리헨션
# =============================================================
# 형식: {키: 값 for 변수 in 반복가능한것}

# 1~5의 제곱을 딕셔너리로
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)                  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 조건 포함
even_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)             # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# 리스트 → 딕셔너리
names = ["Alice", "Bob", "Charlie"]
lengths = {name: len(name) for name in names}
print(lengths)                  # {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# =============================================================
# 10. 유용한 패턴들
# =============================================================

# 빈도수 세기
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1    # 없으면 0, 있으면 +1
print(count)                    # {'apple': 3, 'banana': 2, 'cherry': 1}

# 딕셔너리 합치기 (Python 3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged = d1 | d2                # | 연산자로 합치기
print(merged)                   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 값 기준 정렬
ranking = {"Alice": 90, "Bob": 75, "Charlie": 85}
sorted_by_score = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
print(sorted_by_score)          # [('Alice', 90), ('Charlie', 85), ('Bob', 75)]
