# mortgage.py
#
# Exercise 1.7
# 연습 문제 1.7: 데이브의 주택 담보 대출
# 데이브는 500,000 달러의 30년 고정 이율 주택 담보 대출(mortgage)을 받기로 결정했다.
# 이율은 5%이고 매달 납부할 금액은 2684.11 달러다.
# 다음은 대출 기간 동안 지불할 총액을 계산하는 프로그램이다.

print("연습 문제 1.7: 데이브의 주택 담보 대출")
principal = 500000.0    #원금의 자본금의
rate = 0.05             #이자율
payment = 2684.11       #매월 지급할 금액
total_paid = 0.0        #누적금액

#for x in range(30*12):
loop_count = 1
print("Default scenario")
while principal > 0 :
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    #principal = principal - total_paid
    #if (principal-total_paid < 0):
    #    break
    #print(loop_count, " th", round(total_paid,1))
    loop_count = loop_count + 1

print("Total paid :", round(total_paid, 1), " during", loop_count-1, "months")
print("----------------")

print("연습 문제 1.8: 추가 납입")
print("If I pay $1000 a month for the first 12 months")
principal = 500000.0    #원금의 자본금의
rate = 0.05             #이자율
payment = 2684.11       #매월 지급할 금액
total_paid = 0.0        #누적금액
#for x in range(30*12):
month = 0
while principal > 0 :
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if (month <= 12):
        principal = principal - 1000
        total_paid = total_paid + 1000

print("Total paid :", round(total_paid, 2), " during", month, "months")

print("----------------")
print("연습 문제 1.9: 추가 납입금 계산기")
#추가 납입금을 일반적으로 다룰 수 있게 프로그램을 수정하자. 사용자가 다음 변수를 설정할 수 있게 한다.

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

principal = 500000.0    #원금의 자본금의
rate = 0.05             #이자율
payment = 2684.11       #매월 지급할 금액
total_paid = 0.0        #누적금액
#for x in range(30*12):
month = 0
tmp_payment = 0
while principal > 0 :
    month = month + 1

    #1.9 에서 마지막 달에 초과 납부하는 금액이 생기지 않게 프로그램을 수정해 보라.
    if (principal < payment):
        payment = principal * (1+rate/12)
    #########

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if (month >= extra_payment_start_month and month <= extra_payment_end_month):
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    #월수, 현재까지의 납부액, 남은 원금을 나타내는 테이블을 프린트하게 프로그램을 수정해 보라. 다음과 같이 출력한다.
    if (month < 5 or month > 307):
        print(month, round(total_paid, 2), round(principal, 2))

print("Total paid", round(total_paid, 2), "\nMonths", month)
