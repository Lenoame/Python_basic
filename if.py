x = 15

if x >= 10:
    print(x)

# 파이썬에서 조건문을 작성할 때는 if ~ elif ~ else 문을 이용한다. 그 형태는 다음과 같으며, 조건문을 사용할 때 elif 혹은 else 부분은 경우에 따라서 사용하지 않아도 된다.

if 조건문 1:
    # 조건문 1이 True 일 때 실행되는 코드
elif 조건문 2:
    # 조건문 1에 해당하지 않고, 조건문 2가 True 일 때 실행되는 코드
else:
    # 위의 모든 조건문이 모두 True 값이 아닐 때 실행되는 코드

score = 85

if score >= 80:
    pass # 나중에 작성할 소스코드
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다')

score = 85

if score >= 80: result = "Success"
else: result = "Fail"

#  더 나아가서, 조건부 표현식 Conditional Expression을 이용하면 if ~ else 문을 한 줄에 작성해 사용할 수 있다.abs(
score = 85
result = "Success" if score >= 80 else "Fail"

print(result)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]

print(result)

x = 15
if x > 0 and x < 20:
    print("x는 0 초과 20 미만의 수입니다")

x = 10
if 0 < x < 20:
    print("x는 0 초과 20 미만의 수입니다.")




