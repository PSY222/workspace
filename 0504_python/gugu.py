print('구구단을 몇단을 계산할까요(1~9)?')
num = int(input())
print('구구단 ',num,'단을 계산합니다.')
if num != 0:
 i = 1
 while i < 10:
     print(num,' X ',i,'=',num*i)
     i += 1
else:
    print('구구단 게임을 종료합니다')
