# Python_basic

### 수 자료형
정수형 Integer
 예를 들어 대부분의 언어에서는 HashMap과 같은 별도의 라이브러리를 이용해야 사전 자료형 기능을 구현할 수 있다. 파이썬에는 기본 자료형이 이를 지원하므로 구현이 편리하다는 장점이 있다.
 
실수형 Real Number
 보통 컴퓨터 시스템은 수 데이터를 처리할 때 2진수를 이용하며,  실수를 처리할 때 부동 소수점(Floating-point) 방식을 이용한다. 오늘날 가장 널리 쓰이는 IEEE754 표준에서는 실수형을 저장하기 위해 4바이트, 혹은 8바이트라는 고정된 크기의 메모리를 할당하며, 이러한 이유로 인해 현대 컴퓨터 시스템은 대체로 실수 정보를 표현하는 정확도에 한계를 가진다.
 
 따라서 소수점 값을 비교하는 작업이 필요한 문제라면 실수 값을 비교하지 못해서 원하는 결과를 얻지 못할 수 있다. 이럴 때는 round() 함수를 이용할 수 있다.
 
 round() 함수를 호출할 때는 인자(Argument)를 넣는데 첫 번째 인자는 실수형 데이터이고, 두 번재 인자는 (반올림하고자 하는 위치 -1)이다. 예를 들어 123.456을 소수점 셋째 자리에서 반올림하려면 round(123.456, 2)라고 작성하며 결과는 123.46이다. (두 번째 인자 없이) 인자를 하나만 넣을 때는 소수점 첫째 자리에서 반올림한다.
 
 흔히 코딩 테스트 문제에서는 실수형 데이터를 비교할 때 소수점 다섯 번째 자리에서 반올림한 결과가 같으면 정답으로 인정하는 식으로 처리한다.


### 리스트 자료형
 리스트는 여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용할 수 있다. 파이썬의 리스트는 내부적으로 배열(Array)을 채택하고 있으며, 연결 리스트 자료구조 기능을 포함하고 있어서 append(), remove() 등의 메서드를 지원한다. 파이썬의 리스트는 C++ 의 STL vector와 유사하며, 리스트 대신에 배열 혹은 테이블이라고 부르기도 한다.

리스트 만들기
 리스트는 대괄호[ ] 안에 원소를 넣어 초기화하며, 쉼표(,)로 원소를 구분한다. 리스트의 원소에 접근할 때는 인덱스 값을 괄호 안에 넣는다. 이때 인덱스는 0부터 시작한다. 그리고 비어 있는 리스트를 선언하고자 할 때는 list() 혹은 간단히 대괄호([ ])를 이용할 수 있다.

리스트의 인덱싱과 슬라이싱
 인덱스값을 입력하여 리스트의 특정한 원소에 접근하는 것을 인덱싱(Indexing)이라고 한다. 음의 정수를 넣으면 원소를 거꾸로 탐색하게 된다.

### 리스트 컴프리헨션
 리스트 컴프리헨션을 이용하면 대괄호([ ]) 안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화할 수 있다. 이 경우 한 줄의 소스코드로 리스트를 초기화할 수 있어 매우 간편하다.
 이러한 리스트 컴프리헨션은 코딩 테스트에서 2차원 리스트를 초기화할 때 매우 효과적으로 사용될 수 있다.

 참고로 특정 크기의 2차원 리스트를 초기화할 때는 리스트 컴프리헨션을 이용해야 한다. 만약에 다음과 같이 N * M 크기의 2차원 리스트를 초기화한다면, 의도하지 않은 결과가 나올 수 있다.
 
 실행 결과를 확인해보면 array[1][1]의 값을 5로 바꾸었을 뿐인데, 3개의 리스트에서 인덱스 1에 해당하는 원소들의 값이 모두 5로 바뀐 것을 확인할 수 있다. 이는 내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식되기 때문이다. 따라서 특정한 크기를 가지는 2차원 리스트를 초기화할 때에는 리스트 컴프리헨션을 이용해야 한다는 점을 기억하자.
 
append()
변수명.append()
리스트에 원소를 하나 삽입할 때 사용한다.
시간복잡도 O(1)

sort()
변수명.sort()
기본 정렬 기능으로 오름차순으로 정렬한다.
변수명.sort(reverse = True)
내림차순으로 정렬한다.
시간복잡도 O(NlogN)

reverse()
변수명.reverse()
리스트의 원소의 순서를 모두 뒤집어 놓는다.
시간복잡도 O(N)

insert()
변수명.insert(삽입할 위치 인덱스, 삽입할 값)
특정한 인덱스 위치에 원소를 삽입할 때 사용한다.\
시간복잡도 O(N)

count()
변수명.count(특정 값)
리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용한다.
시간복잡도 O(N)

remove()
변수명.remove(특정 값)
특정한 값을 갖는 원소를 제거하느데, 값을 가진 원소가 여러 개면 하나만 제거한다.
시간복잡도 O(N)

이 중에서 insert() 함수와 append(), remove()를 특히 더 눈여겨 두자

### 문자열 자료형
문자열 초기화
 기본적으로 문자열을 큰따옴표로 구성하는 경우, 내부적으로 작은따옴표를 포함할 수 있다. 반대로 문자열을 작은따옴표로 구성하는 경우, 내부적으로 큰따옴표를 이용할 수 있다. 혹은 백슬래시(\)를 사용하면, 큰따옴표나 작은따옴표를 문자열에 원하는 만큼 포함시킬 수 있다.
 프로그래밍 문법에서는 백슬래시와 같은 문자를 '이스케이프 문자'로 정해두고 큰따옴표를 출력하는 등의 특별한 목적으로 사용한다.

문자열 연산
 파이썬은 문자열에 대한 연산도 지원하는데 문자열을 처리할 때 유용하게 사용할 수 있다. 예를 들어 문자열 변수에 덧셈(+)을 이용하면 단순히 문자열이 더해져서 연결된다.
 파이썬의 문자열은 내부적으로 리스트와 같이 처리된다. 문자열은 여러 개의 문자가 합쳐진 리스트라고 볼 수 있다. 따라서 문자열 데이터에 대해서도 마찬가지로 인덱싱과 슬라이싱을 이용할 수 있다.

### 튜플 자료형
파이썬의 튜플 자료형은 리스트와 거의 비슷한데 다음과 같은 차이가 있다.

1. 튜플은 한 번 선언된 값을 변경할 수 없다.
2. 리스트는 대괄호([ ])를 이용하지만, 튜플은 소괄호(())를 이용한다.

튜플의 값(1, 2, 3, 4)는 그대로 출력되는 것을 확인할 수 있다. 하지만 튜플의 특정한 값을 변경하려고 할 때는 오류 메세지가 출력된다. 오류의 내용에서는 원소의 대입 Item Assignment이 불가능하다는 메시가 출력되고 있다. 말 그대로 대입 연산자 (=)를 사용하여 값을 변경할 수 없다는 의미이다.
 튜플 자료형은 그래프 알고리즘을 구현할 때 자주 사용된다. 예를 들어 다익스트라 최단 경로 알고리즘처럼 최단 경로를 찾아주는 알고리즘의 내부에서는 우선순위를 큐를 이용하는데 해당 알고리즘에서 우선순위 큐에 한 번 들어간 값은 변경되지 않는다. 그래서 그 우선순위 큐에 들어가는 데이터를 튜플로 구성하여 소스코드를 작성한다. 이렇게 알고리즘을 구현하는 과정에서 튜플을 이용하게 되면 혹여나 자신이 알고리즘을 잘못 작성함으로써 변경하면 안 되는 값이 변겨오디고 있지는 않은지 체크할 수 있다. 또한 튜플은 리스트에 비해 상대적으로 공간 효율적이고, 일반적으로 각 원소의 성질이 서로 다를 때 주로 사용한다. 흔히 다익스트라 최단 경로 알고리즘에서는 '비용''과 '노드 번호'라는 서로 다른 성질의 데이터를 (비용, 노드 번호)의 형태로 함께 튜플로 묶어서 관리하는 것이 관례이다.
 
### 사전 자료형
 사전 자료형은 키 Key와 값 Value의 쌍을 데이터로 가지는 자료형이다. 앞서 다루었던 리스트나 튜플은 값을 순차적으로 저장한다는 특징이 있다. 하지만 사전 자료형은 키—값 쌍을 데이터로 가진다는 점에서, 우리가 원하는 변경 불가능한 데이터를 키로 사용할 수 있다. * 파이썬의 사전 자료형을 이용한 매우 효과적인 사례가 있다. 사전 자료형이 사용되는 대표적인 예시는 사전 Dictionary이다.
 
키(Key) — 값(Value)
사과 : Apple
바나나 : Banana
코코넛 : Coconut
 파이썬의 사전 자료형은 내부적으로 '해시 테이블 Hash Table'을 이용하므로 기본적으로 데이터의 검색 및 수정에 있어서 O(1)의 시간에 처리할 수 있다. 
 변경 불가능한 자료형이란 수 자료형, 문자열 자료형, 튜플 자료형과 같이 한 번 초기화되면 변경이 불가능한 자료형을 의미한다. 흔히 사용되지는 않지만, 튜플 자료형이 사전 자료형의 키로 사용되기도 하는데, 이는 'Q 22 블록 이동하기' 문제 풀이에서 사용된다.
 
 사전 자료형에 특정한 원소가 있는지 검사할 때는 '원소 in 사전'의 형태를 사용할 수 있다. 이는 리스트나 튜플에 대해서도 사용할 수 있는 문법이다.

 파이썬에서 리스트, 문자열, 튜플 등 원소들을 차례대로 반복할 수 있는 자료형을 Iterable 자료형이라고 한다. 이러한 Iterable 자료형들은 그 내부에 원소들을 포함하는 컨테이너 역할도 하는 것이 대부분이기에 in 문법도 사용이 가능하다.

사전 자료형 관련 함수
 키 데이터만 뽑아서 리스트로 이용할 때는 keys()함수를 이용하며, 값 데이터만을 뽑아서 리스트로 이용할 때는 values() 함수를 이용한다.
 
### 집합 자료형
집합 자료형 소개
 파이썬에서는 집합 Set을 처리하기 위한 집합 자료형을 제공하고 있다. 집합은 기본적으로 리스트 혹은 문자열을 이용해서 만들 수 있는데, 집합은 다음과 같은 특징이 있다.
 
1. 중복을 허용하지 않는다.
2. 순서가 없다.

리스트나 튜플은 순서가 있음.
 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다는 특징이 있다. 이와 더불어 집합 자료형에서는 키가 존재하지 않고, 값 데이터만을 담게 된다. 특정 원소가 존재하는지를 검사하는 연산의 시간 복잡도는 사전 자료형과 마찬가지로 O(1)이다.
 특히 '특정한 데이터가 이미 등장한 적이 있는지 여부'를 체크할 때 매우 효과적으로 사용됨. 집합 자료형을 초기화할 때는 set() 함수를 이용하거나, 중괄호({})안에 각 원소를 콤마( , )를 기준으로 구분해서 넣으면 된다.
 
집합 자료형의 연산
 기본적인 집합 연산으로는 합집합, 교집합, 차집합 연산이 있다. 파이집합 자료형 데이터 사이에서 합집합을 계산할 때는 '|'를 이용한다. 또한 교집합은 '&', 차집합은 '—'를 이용한다.
 
집합 자료형 관련 함수
 하나의 집합 데이터에 값을 추가할 때는 add() 함수를 이용할 수 있다. update() 함수는 여러 개의 값을 한꺼번에 추가하고자 할 때 사용한다. 그리고 특정한 값을 제거할 때는 remove() 함수를 이용할 수 있다.. 이때 add(), remove() 함수는 모두 시간 복잡도가 O(1)이다.


# 내장함수와 라이브러리

내장함수 : print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리이다. 파이썬 프로그램을 작성할 때 없어서는 안 되는 필수적인 기능을 포함하고 있다.

itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리이다. 순열과 조합 라이브러리를 제공한다.

heapq : 힙(Heap) 기능을 제공하는 라이브러리이다. 우선순위 큐 기능을 구현하기 위해 사용한다.

bisect : 이진탐색(Binary Search) 기능을 제공하는 라이브러리이다.

collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리이다.

math : 필수적인 수학적 기능을 제공하는 라이브러리이다. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함하고 있다.

### 내장함수 

sum()함수는 리스트와 같은 iterable 객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환한다.

- 파이썬에서 iterable 객체는 반복 가능한 객체를 말한다. 리스트, 사전 자료형, 튜플 자료형 등이 이에 해당한다.

min()함수는 파라미터가 2개 이상 들어왔을 때 가장 작은 값을 반환한다. 

max() 함수는 파라미터가 2개 이상 들어왔을 때 가장 큰 값을 반환한다.

eval()함수는 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.

sorted() 함수는 iterable 객체가 들어왓을 때, 정렬된 결과를 반환한다. key 속성으로 정렬 기준을 명시할 수 있으며, reverse 속성으로 정렬된 결과 리스트를 뒤집을지의 여부를 설정할 수 있다.

파이썬에서는 리스트의 원소로 리스트나 튜플이 존재할 때 특정한 기준에 따라서 정렬을 수행할 수 있다. 정렬 기준은 key 속성을 이용해 명시할 수 있다.

### itertools

itertools는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다. 제공하는 클래스는 매우 다양하지만, 코딩 테스트에서 가장 유용하게 사용할 수 있는 클래스는 permutations, combinations이다. 참고로 순열과 조합에 대한 설명 부록 B에서도 추가로 다루고 있다.

permutations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)을 계산해준다. permutations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.

combinations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 경우(조합)를 계산한다. combinations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다. 

### heapq

파이썬에서는 힙 Heap 기능을 위해 heapq 라이브러리를 제공한다. heapq는 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용된다. heapq 외에도 PriorthQueue 라이브러리를 사용할 수 있지만, 코딩 테스트 환경에서는 보통 heapq가 더 빠르게 동작하므로 heapq를 이용하도록 하자.

파이썬의 힙은 최소 힙 Min Heap 으로 구성되어 있으므로 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다. 보통 최소 힙 자료구조의 최상단 원소는 항상 '가장 작은' 원소이기 때문이다.

힙에 원소를 삽입할 때는 heapq.heappush() 메서드를 이용하고, 힙에서 원소를 꺼내고자 할 때는 heapq.heappop() 메서드를 이용한다. 힙 정렬 Heap Sort을 heapq로 구현하는 예제를 통해 heapq 사용 방법을 알아보자.

또한 파이썬에서는 최대 힙 Max Heap을 제공하지 않는다. 따라서 heapq 라이브러리를 이용하여 최대 힙을 구현해야 할 때는 원소의 부호를 임시로 변경하는 방식을 사용한다. 힙에 원소를 삽입하기 전에 잠시 부호를 반대로 바꾸었다가, 힙에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꾸면 된다.

### bisect

파이썬에서는 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공한다. bisect 라이브러리는 '정렬된 배열' 에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다. bisect 라이브러리에서는 bisect_left() 함수와 bisect_right() 함수가 가장 중요하게 사용되며, 이 두 함수는 시간 복잡도 O(NlogN)에 동작한다.

- bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
- bisect_right(a, x) : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽에 인덱스를 찾는 메서드

예를 들어 정렬된 리스트 [1,2,4,4,8]이 있을 때, 새롭게 데이터 4를 삽입하려고 가정하자. 이때 bisect_left(a, 4)와 bisect_right(a, 4)는 각각 인덱스값으로 2와 4를 반환한다.

또한 bisect_left() 함수와 bisect_right() 함수는 '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때, 효과적으로 사용될 수 있다.

아래의 count_by_range(a, left_value, right_value) 함수를 확인해보자. 이는 정렬된 리스트에서 값이 [left_value, right_value]에 속하는 데이터의 개수를 반환한다. 다시 말해 원소의 값을 x라고 할 때, left_value ≤ x ≤ right_value인 원소의 개수를 O(NlogN) 으로 빠르게 계산할 수 있다.

# 조건문
조건문은 프로그램을 작성할 때 프로그램의 흐름을 제어하는 문법이다. 조건문을 이용하면 조건에 따라서 프로그램의 로직을 설정할 수 있다.

### in 연산자와 not in 연산자

- X in 리스트 : 리스트 안에 X가 들어가 있을 때 참(True)이다.

- X not in 문자열 : 문자열 안에 X가 들어가 있지 않을 때 참(True)이다.

또한 파이썬에서는 조건문의 값이 참(True)이라고 해도, 아무것도 처리하고 싶지 않을 때 pass 문을 이용할 수 있다. 예를 들어 코드를 작성하면서 디버깅하는 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분은 비워놓고 싶을 때가 있다.

그리고 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있다.

특히 조건부 표현식은 리스트에 있는 원소의 값을 변경해서, 또 다른 리스트를 만들고자 할 때 매우 간결하게 사용할 수 있다. 예를 들어 리스트에서 특정한 원소의 값만을 없앤다고 해보자.
 
### 파이썬 조건문 내에서의 부등식
 다른 언어와 달리 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용할 수 있다. 예를 들어 "x > 0 and x < 20" 과 "0 < x < 20" 은 같은 결과를 반환한다. 다만, 파이썬이 아닌 대부분의 프로그래밍 언어에서는 단순히 "0 < x < 20" 이라고 하면, 의도하지 않은 결과가 반환될 수 있다. 다시 말해 파있너에서는 다음의 두 조건문이 동일하다.

# 반복문
반복문은 특정한 소스코드를 반복적으로 실행하고자 할 때 사용할 수 있다. 파이썬에서는 while문과 for문이 있는데 어떤 것을 사용해도 상관 없음. 하지만 코딩 테스트에서의 실제 사용 예시를 확인해보면, 대부분의 경우에서 for문이 더 소스코드가 짧은 경우가 많다.

### while문
while문은 조건문이 참일 때에 한해서, 반복적으로 코드가 수행된다. 조건문 설정에 따라 해당 블록을 영원히 반복할 수도 있는데, 이를 무한 루프 Infinite Loop라고 한다.

### for문
리스트를 사용하는 대표적인 for문의 구조는 다음과 같은데, in 뒤에 데이터에 오는 포함되어 있는 모든 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문한다. in 뒤에 오는 데이터로는 리스트, 튜플, 문자열 등이 사용될 수 있다.

for문에서  수를 차례대로 나열할 때는 range()를 주로 쓰는데 range(시작 값, 끝 값 + 1) 형태로 쓰인다. 예를 들어 1부터 9까지의 모든 수를 담고자 한다면 range(1, 10)이라고 작성한다.

또한 range()의 값으로 하나의 값만을 넣으면, 자동을 시작 값은 0이 된다. 주로 리스트나 튜플 데이터의 모든 원소를 첫 번째 인덱스부터 방문해야 할 때 이 방법을 사용한다.

반복문 안에서 continue를 만나면 프로그램의 흐름은 반복문의 처음으로 돌아간다.

반복문은 얼마든지 중첩해서 사용할 수 있다. 예를 들어 2중 반복문이 사용되어야 하는 대표적인 예시는 구구단 예시이다. 실제로 중첩된 반복문은 코딩 테스트에서도 '플로이드 워셜 알고리즘', '다이나믹 프로그래밍' 등의 알고리즘 문제에서 매우 많이 사용된다.

