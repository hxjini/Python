#else를 사용하여 두 방향으로 분기하기
#else는 if와 들여쓰기 규칙이 같음
kor, eng, mat, sci=map(int,input().split())
if(0<=kor<=100) and (0<=eng<=100) and (0<=mat<=100) and (0<=sci<=100):
    avg = (kor+eng+mat+sci) / 4
    if avg>=80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')