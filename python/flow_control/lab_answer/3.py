# 문제 3. 면적 단위 변환기

"""
사용자가 제곱미터(m²) 단위로 입력한 토지의 면적을 평방피트(ft²)와
에이커(ac) 단위로 변환해주는 프로그램을 작성하세요.

* 변환 공식
- 1제곱미터 (m²) = 10.7639 평방피트 (ft²)
- 1에이커 (ac) = 4046.86 제곱미터 (m²)

* 요구사항
- 두 개의 함수를 정의하여 각 단위로의 변환을 담당합니다.
  - convert_to_square_feet: 제곱미터를 평방피트로 변환합니다.
  - convert_to_acres: 제곱미터를 에이커로 변환합니다.
- 사용자로부터 토지의 면적을 제곱미터(m²) 단위로 입력 받습니다.
- 입력받은 면적이 음수일 경우, 변환 대신 "잘못된 입력입니다"를 출력합니다.

* 실행 결과
- 첫 번째 실행
입력 -> 토지의 면적을 제곱미터(m²) 단위로 입력하세요: 10
출력 ->
10.0 제곱미터는 107.639 평방피트입니다.
10.0 제곱미터는 0.0024710516301527604 에이커입니다.

- 두 번째 실행
입력 -> 토지의 면적을 제곱미터(m²) 단위로 입력하세요: -2
출력 -> 잘못된 입력입니다.
"""

def convert_to_square_feet(square_meters):
    # 제곱미터를 평방피트로 변환한다.
    return square_meters * 10.7639

def convert_to_acres(square_meters):
    # 제곱미터를 에이커로 변환한다.
    return square_meters / 4046.86

# 사용자 입력 받기
square_meters = float(input("토지의 면적을 제곱미터(m²) 단위로 입력하세요: "))

# 음수 입력 처리
if square_meters < 0:
    print("잘못된 입력입니다.")

# 변환 함수 호출과 결과 출력
else:
    square_feet = convert_to_square_feet(square_meters)
    acres = convert_to_acres(square_meters)
    print(f"{square_meters} 제곱미터는 {square_feet} 평방피트입니다.")
    print(f"{square_meters} 제곱미터는 {acres} 에이커입니다.")
