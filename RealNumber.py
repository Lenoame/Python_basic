#실수형 Real Number 은 소수점 아래의 데이터를 포함하는 수 자료형으로 
#파이썬에서는 변수에 소수점을 붙인 수를 대입하면 실수형으로 처리한다. 
#소수부가 0이거나, 정수부가 0인 소수는 0을 생략하고 작성할 수 있다.

#양의 실수
from typing_extensions import runtime


a = 157.93
print(a)

#음의 실수
b = -1837.2
print(b)

#소수부가 0일 때 0을 생략
c = 5.
print(c)

#정수부가 0일 때 0을 생략
d = -.7
print(d)

# 10억의 지수 표현 방식
a = 1e9
print(a)

# 752.5
a = 75.25e1
print(a)

# 3.954
a = 3954e-3
print(a)

a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)


