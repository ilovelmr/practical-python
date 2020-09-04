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
print("bill_thickness:", bill_thickness, ", sears_height:",sears_height, ", num_bills:",num_bills)
while (num_bills * bill_thickness) < sears_height:
    #print (day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills*2

print ('Number of days', day, end= "")
print (', Number of bills', num_bills, end="")
print(', Final height', num_bills * bill_thickness)


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


################
# 숫자 타입
# 파이썬에는 네 가지 숫자 타입이 있다.

#불린
#정수
#부동소수점
#복소수(허수)
a = True
b = False
c = 4 + True
d = False
if d == 0:
    print ('d is False')

#####################
# int : 임의의 크기에 밑수(base)가 있는 부호 있는(signed) 값이다.
a = 37
b = -299392993727716627377128481812241231
c = 0x7fa8      # 16진수
d = 0o253       # 8진수
e = 0b10001111  # 2진수

'''
x + y      덧셈
x - y      뺄셈
x * y      곱셈
x / y      나눗셈(부동소수점수를 생성)
x // y     Floor 나눗셈(정수를 생성)
x % y      모듈로(나머지)
x ** y     제곱
x << n     왼쪽으로 비트 시프트(shift)
x >> n     오른쪽으로 비트 시프트
x & y      AND 비트 연산
x | y      OR 비트 연산
x ^ y      XOR 비트 연산
~x         NOT 비트 연산
abs(x)     절댓값
'''

# 부동소수점(float) : 십진수 또는 지수 표기법을 사용해 부동소수점수를 지정한다.
# 부동소수점은 네이티브 CPU 표현 IEEE 754를 사용해 배정밀도(double precision)로 나타낸다.
# C 프로그래밍 언어의 double 타입과 같다.
# 정밀도는 17 자리
# -308에서 308까지

a = 37.45
b = 4e5 # 4 x 10**5 또는 400,000
c = -1.345e-10

#>>> a = 2.1 + 4.2
#>>> a == 6.3
#False
#>>> a
#6.300000000000001
# 이것은 파이썬 이슈가 아니라, CPU의 부동소수점 하드웨어 때문이다.
'''
x + y      덧셈
x - y      뺄셈
x * y      곱셈
x / y      나눗셈
x // y     Floor 나눗셈
x % y      모듈로
x ** y     제곱
abs(x)     절댓값
'''

#리터럴 텍스트(Literal Text) 표현
"""
'\n'      라인 피드(Line feed)
'\r'      캐리지 리턴(Carriage return)
'\t'      탭(Tab)
'\''      리터럴 작은 따옴표(Literal single quote)
'\"'      리터럴 큰 따옴표(Literal double quote)
'\\'      리터럴 백슬래시(Literal backslash)
"""

desc = """
a = '\\xf1'          # a = 'ñ'
b = '\\u2200'        # b = '∀'
c = '\\U0001D122'    # c = '𝄢'
d = '\\N{FOR ALL}'   # d = '∀'
"""
print(desc)


# 문자열 인덱싱(String Indexing)
# 문자열은 문자에 액세스함에 있어서 배열(array)과 비슷하게 작동한다.
# 0부터 시작하는 정수 인덱스(index)를 사용한다.
# 음수 인덱스는 문자열의 끝에서부터 상대적 위치를 가리킨다.
a = 'Hello World'
b = a[0]          # 'H'
c = a[4]          # 'o'
d = a[-1]         # 'd'(문자열의 끝)
print (a)
print (b, c, d)

d = a[:5]     # 'Hello'
e = a[6:]     # 'world'
f = a[3:8]    # 'lo wo'
g = a[-5:]    # 'world'


# https://wikidocs.net/84384
# 문자열 연산
# 이어붙이기(concatenation), 길이(length), 멤버십(membership), 복제(replication).

# 이어붙이기(+)
a = 'Hello' + 'World'   # 'HelloWorld'
b = 'Say ' + a          # 'Say HelloWorld'

# 길이(len)
s = 'Hello'
len(s)                  # 5

# 멤버십 테스트(`in`, `not in`)
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True

# 복제(s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'

print("문자열 연산 : ", '''
s.endswith(suffix)     # 문자열이 suffix로 끝나는지 확인
s.find(t)              # s에서 t가 처음 나타나는 곳
s.index(t)             # s에서 t가 처음 나타나는 곳
s.isalpha()            # 문자가 영문자인지 여부
s.isdigit()            # 문자가 숫자인지 여부
s.islower()            # 문자가 소문자인지 여부
s.isupper()            # 문자가 대문자인지 여부
s.join(slist)          # s를 구분자(delimiter)로 삼아 문자열의 리스트를 붙이기(join)
s.lower()              # 소문자로 변환
s.replace(old,new)     # 텍스트 교체
s.rfind(t)             # 문자열의 끝에서부터 t를 검색
s.rindex(t)            # 문자열의 끝에서부터 t를 검색
s.split([구분자])       # 문자열을 분할해 부분 문자열의 리스트를 만듦
s.startswith(prefix)   # 문자열이 prefix로 시작하는지 확인
s.strip()              # 앞뒤의 공백을 제거
s.upper()              # 대문자로 변환
'''
)

# 문자열의 변경가능성(Mutability)
# 문자열은 "변경불가능(immutable)", 즉 읽기 전용이다. 한번 생성하면 값이 바뀌지 않는다.
# 문자열 데이터를 조작하는 모든 연산과 메서드는 항상 새로운 문자열을 생성한다.

# 원시 문자열(Raw String)
'''
원시 문자열은 백슬래시를 해석하지 않는 문자열 리터럴이다. 소문자 "r"을 앞에 붙여 원시 문자열임을 나타낸다.
문자열은 입력한 그대로의 리터럴 텍스트다.
백슬래시가 특별히 중요할 때 이것을 사용하면 편리하다.
예: 파일명, 정규 표현식(regular expression) 등
>>> rs = r'c:\newdata\test' # 원시(백슬래시를 해석하지 않음)
>>> rs
'c:\\newdata\\test'
'''

#f 문자열(f-String)
'''
포매팅된 표현식 대체가 있는 문자열이다. Python 3.6 이상에서만 됨.
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> a = f'{name:>10s} {shares:10d} {price:10.2f}'
>>> a
'       IBM        100      91.10'
>>> b = f'Cost = ${shares*price:0.2f}'
>>> b
'Cost = $9110.00'
>>>
'''

'''
#문자열이 읽기 전용이라고 했는데,
#이 예에서는 원래의 문자열을 수정해 규칙을 위반하는 것처럼 보일 수도 있다.
#그런 것이 아니다.
#문자열에 대한 연산은 완전히 새로운 문자열을 매번 생성한다.
#변수명 심벌(symbol)이 재할당되면, 그것은 새로 생성된 문자열을 가리킨다.
#사용하지 않는 문자열은 삭제된다.
'''


# 연습 문제 1.18: 정규 표현식(Regular Expressions)
#기본 문자열 연산은 고급 패턴 매칭을 지원하지 않지만, 파이썬의 re 모듈을 가지고 정규 표현식을 사용할 수 있다. 정규 표현식은 그 자체로 큰 주제이지만 여기서는 간단한 예를 들겠다.
'''
>>> text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
>>> # 날짜가 있는 곳을 모두 찾음
>>> import re
>>> re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']
>>> # 날짜가 있는 곳을 모두 찾아 text로 교체
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2018-3-27. Tomorrow is 2018-3-28.'
>>>
re 모듈에 대한 자세한 정보는 공식 문서 https://docs.python.org/library/re.html을 참조하라.
'''


#파이썬 환경에 따라, 탭 자동완성을 통해 리스트를 볼 수 있을 수도 있다. 다음과 같이 해 보라.
'''
>>> s = 'hello world'
>>> s.<tab key>
>>>
'''


# https://wikidocs.net/84384
# 1.5 LIST
# 주의: 리스트는 수학 연산을 위해 설계한 것이 아니다.
'''
>>> nums = [1, 2, 3, 4, 5]
>>> nums * 2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> nums + [10, 11, 12, 13, 14]
[1, 2, 3, 4, 5, 10, 11, 12, 13, 14]
특히 리스트는 매트랩(MATLAB), 옥타브(Octave), R 등의 벡터나 행렬을 나타내지 않는다.
그런 용도로 사용할 수 있는 패키지가 따로 있다.(예: numpy)
'''


# 연습 문제 1.25: 온갖 것들의 리스트
# 리스트는 어떤 종류의 객체든 담을 수 있고, 다른 리스트를 담을 수도 있다(예: 중첩된 리스트). 다음과 같이 시도해보라.
'''
>>> nums = [101, 102, 103]
>>> items = ['spam', symlist, nums]
>>> items
['spam', ['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
출력을 잘 들여다 보라. items는 세 개의 원소를 가진 리스트다. 첫 번째 원소는 문자열이지만,
나머지 두 개의 원소는 리스트다.

여러 가지 인덱싱 연산자를 사용해 중첩된 리스트의 항목에 액세스할 수 있다.

>>> items[0]
'spam'
>>> items[0][0]
's'
>>> items[1]
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[1][1]
'RHT'
>>> items[1][1][2]
'T'
>>> items[2]
[101, 102, 103]
>>> items[2][1]
102
>>>
매우 복잡한 리스트 구조를 만드는 것이 기술적으로는 가능하지만, 단순하게 만드는 것이 좋다.
리스트의 항목은 모두 같은 종류의 값으로 구성하는 것이 일반적이다.
예를 들어, 숫자만으로 리스트를 구성하거나, 텍스트 문자열만으로 리스트를 구성한다.
같은 리스트에 여러 종류의 데이터를 섞다보면 머리가 터질 수 있으니 될 수 있으면 피하자.
'''


#https://github.com/ilovelmr/practical-python/blob/master/Notes/01_Introduction/06_Files.md
try :
    with open('./Data/portfolio.csv', 'rt') as f:
        x = 1
        for line in f:
            print(x, line, end="")
            x = x + 1
except:
    print("An exception occurred")

'''
>>> f = open('./Work/Data/portfolio.csv', 'rt')
>>> headers = next(f).split(",")
>>> headers
['name', 'shares', 'price\n']
>>> for line in f:
...     row = line.split(",")
...     print (row)
...
['"AA"', '100', '32.20\n']
['"IBM"', '50', '91.10\n']
['"CAT"', '150', '83.44\n']
['"MSFT"', '200', '51.23\n']
['"GE"', '95', '40.37\n']
['"MSFT"', '50', '65.10\n']
['"IBM"', '100', '70.44\n']
>>>
'''

# file 처리 중 CSV 파일을 다루는 건 Pandas https://pandas.pydata.org 가 있음.
