# 문제 4. 평균 점수와 학점 등급 계산 프로그램

"""
학생들의 세 과목 점수를 입력 받아 평균 점수를 계산하고,
평균에 따른 학점 등급을 부여하는 프로그램을 만듭니다.

* 학점 등급 기준
- A: 90점 이상
- B: 80점 이상 90점 미만
- C: 70점 이상 80점 미만
- D: 60점 이상 70점 미만
- F: 60점 미만

* 요구사항
- 사용자로부터 수학, 과학, 영어의 점수를 입력받습니다.
- calculate_average 함수에서 평균 점수를 계산하고 학점 등급을 반환합니다.
- 각 과목의 점수와 함께 평균 점수 및 해당하는 학점 등급을 출력합니다.

* 실행 결과
- 첫 번째 실행
입력 ->
수학 점수를 입력하세요: 50
과학 점수를 입력하세요: 60
영어 점수를 입력하세요: 70
출력 -> 평균 점수는 60.0점이고, 학점은 D입니다.

- 두 번째 실행
입력 ->
수학 점수를 입력하세요: 80
과학 점수를 입력하세요: 90
영어 점수를 입력하세요: 100
출력 -> 평균 점수는 90.0점이고, 학점은 A입니다.
"""

def calculate_average(math_score, science_score, english_score):
    # 세 과목의 평균을 계산한다.
    average = (math_score + science_score + english_score) / 3

    # 평균 점수에 따라 학점 등급을 결정한다.
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    return average, grade

# 사용자 입력 받기
math_score = float(input("수학 점수를 입력하세요: "))
science_score = float(input("과학 점수를 입력하세요: "))
english_score = float(input("영어 점수를 입력하세요: "))

# 평균 계산 및 학점 등급 출력
average, grade = calculate_average(math_score, science_score, english_score)
print(f"평균 점수는 {average}점이고, 학점은 {grade}입니다.")
