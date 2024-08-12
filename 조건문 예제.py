x=int(input())
if x==1:
  a = int(input('1-초등, 2-중등, 3-고등 : '))
  if a==1:
    print('학생이며 초등학생입니다.')
  elif a==2:
    print('학생이며 중학생입니다.')
  elif a==3:
    print('학생이며 고등학생입니다.')
  else:
    print('잘못된 입력')
else:
  print('학생이 아닙니다.')
  
x = int(input('금액을 입력하세요 : '))
a = int(input('음료선택: 1-콜라 600원, 2-사이다 700원, 3-환타 800원 : '))
if a ==1:
  print('잔액:', x-600)
elif a ==2:
  print('잔액:', x-700)
elif a==3:
  print('잔액:', x-800)
else:
  print('잘못된 입력')