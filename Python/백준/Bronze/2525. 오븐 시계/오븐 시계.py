A, B = map(int, input().split())  # 현재 시각 A(시), B(분)
C = int(input())  # 요리하는 데 걸리는 시간 C(분)

B += C  # B에 C분을 추가

if B >= 60:  # 60분 이상이면 시간 증가 필요
    end_time = B // 60  # 증가할 시간 계산
    B = B % 60  # 60분이 넘는 부분을 제거하고 0~59 범위로 조정
    A += end_time  # A에 증가한 시간 반영

if A >= 24:  # 24시간을 넘으면 조정
    A = A % 24

print(A, B)