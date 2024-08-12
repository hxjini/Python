#초기식부터 시작하여 조건식을 판별함
#조건식이 참(True)이면 반복할 코드와 변화식을 함께 수행함
#조건식을 판별하여 참이면 코드를 계속 반복하고, 거짓(이면 반복문을 끝낸 뒤 다음 코드를 실행함

#while 예제
i = 0
while i < 100:
  print('Hello, world!')
i += 1

i = 1
while i <= 100:
  print('Hello, world!', i)
i += 1

x = int(input('정수 입력 : '))
sum = 0
i = 1
while i <= x:
  sum += i
  i += 1
print(sum)

x = int(input())
i = 1
while i <= 9:
  print(3,'*', i, '=', 3*i)
  i += 1

kor = [70,60, 55, 75, 95, 90, 80, 85, 100]
avg = 0
i = 0
while i < len(kor):
  avg += kor[i]
  i += 1
print(avg/len(kor))

i = 1
x = 1
while i <= 20:
  x = 2 * x
  i += 1
print('2의',i-1,'승은',x,'입니다.')