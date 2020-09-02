# 주석은 #으로 표시하며, 해당 행의 끝까지다.
# 타입(Type): 변숫값의 타입을 선언할 필요가 없다. dynamically typed
# 변수와 관련된 타입은 변수명이 아니라 오른쪽에 무엇이 오느냐에 따라 결정된다.
# 파이썬은 대문자와 소문자를 구별한다
# 언어의 키워드는 모두 소문자다.

# 들여쓰기는 함께 있는 문장들의 그룹을 나타낸다. 블록의 개념이라 생각하면 됨

import urllib.request
from xml.etree.ElementTree import parse

try :
    u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')

    doc = parse(u)
    for pt in doc.findall('.//pt'):
        print(pt.text)
except:
    print("An exception occurred")

'''
HTTP 프락시 서버가 필요한 작업 환경이라면 이 연습 문제를 풀기 위해 HTTP_PROXY 환경변수를 설정해야 할 수도 있다. 예:

>>> import os
>>> os.environ['HTTP_PROXY'] = 'http://yourproxy.server.com'
>>>
'''
#################
'''
어느 날 아침, 당신은 시카고의 시어스 타워(Sears tower) 근처를 거닐다가
보도에 1 달러 지폐를 한 장 올려뒀다.
그 후 매일 외출할 때마다 그 위에 지폐를 얹어 탑을 쌓으며, 높이는 매일 두 배로 불어난다.
돈으로 쌓은 탑의 높이가 시어스 타워의 높이와 같아지려면 시간이 얼마나 걸릴까?
'''

bill_thickness = 0.11 * 0.001 # assumtion thick of bill
sears_height = 442 # assumtion of the Sears tower's height
num_bills = 1
day = 1
while (num_bills * bill_thickness) < sears_height:
    print (day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills*2

print ('Number of days', day)
print ('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)


################
a = 3
b = 2
print ("a =", a,", b =", b)
if a > b:
    print('Computer says no')
elif a == b:
    print('Computer says yes')
else:
    print('Computer says maybe')

################

# 개행 문자를 프린트하고 싶지 않으면 다음과 같이 한다.
print('Hello', end=' ')
print('My name is', 'Jake')

# 사용자가 타이핑한 입력의 행을 읽으려면 input() 함수를 사용한다.
# input은 사용자에게 프롬프트를 프린트하고 사용자의 응답을 반환한다.
# 이것은 작은 프로그램, 연습 문제, 간단한 디버깅 등에 적합하다. 실제 프로그램에서는 그리 많이 사용하지 않는다.
# name = input('Enter your name:')
# print('Your name is', name)


################
# 때로는 빈 코드 블록을 지정하고 싶을 때가 있다. 이때 사용할 수 있는 키워드가 pass다.
if a > b:
    pass
else:
    print('Computer says false')
