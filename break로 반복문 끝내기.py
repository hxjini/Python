x = int(input())
i = 0
while x >= 0:
  x = x - 1350
  if x < 0:
    print('잔액 부족')
    break
print(x)

#break로 반복문 끝내기
i = 0
total = 0
while True:
  i = i + 1
  total = total + i
  print(i)
  if i == 100:
    break
print(total)