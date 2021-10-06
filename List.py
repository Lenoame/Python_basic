a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 인덱스 4, 즉 다섯 번째 원소에 접근
print(a[4])

# 빈 리스트 선언 방법 1)
a = list()
print(a)

# 빈 리스트 선언 방법 2)
a = []
print(a)


# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 리스트의 인덱싱과 슬라이싱

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 뒤에서 첫 번째 원소 출력
print(a[-1])

# 뒤에서 세 번째 원소 출력
print(a[-3])

# 네 번째 원소 값 변경a
a[3] = 7
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 두 번째 원소부터 네 번째 원소까지
print(a[1:4])


# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)


# 위 소스코드를 일반적인 소스코드로 작성한 코드
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)

# 리스트 컴프리헨션을 이용했을 때의 소스코드가 훨씬 짧고 간결한 것을 알 수 있음.

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]

print(array)

# N * M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# 언더바(_) 는 어떤 역할일까요?
# 파이썬 자료구조/ 알고리즘에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 자주 사용한다.
# 예를  들어 1부터 9까지의 자연수를 더할 때는 왼쪽 예시처럼 작성하지만, 단순히 "Hello World" 를 5번 출력할 때는 오른쪽처럼
# 언더바(_)를 이용하여 무시할 수 있다.

summary = 0

for i range(1, 10):
    summary += i
print(summary)

for _ in range(5):
    print("Hello World")




