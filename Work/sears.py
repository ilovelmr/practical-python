# sears.py
# 오류 메시지를 읽는 것은 파이썬 코드에서 중요한 부분이다.
# 프로그램이 크래시된다면 트레이스백(traceback) 메시지에서
# 마지막 행을 읽으면 프로그램이 크래시된 진짜 이유를 알 수 있다.
# 그 위에는 소스 코드의 일부가 있으며 파일명과 행 번호가 있다.

#코드의 몇 번째 행에 오류가 있는가?
#무엇이 잘못되었는가?
#오류를 수정하라
#프로그램을 성공적으로 실행하라

bill_thickness = 0.11 * 0.001    # 미터(0.11 mm)
sears_height   = 442             # 높이(미터)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = days + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
