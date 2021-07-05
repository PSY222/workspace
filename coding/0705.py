# invest = round(int(input("투자액:")))
# term = int(input("투자기간:"))
# percent = input("전일 대비 가치 변동:").split(' ')

original = 10000
invest = 10000
term = 4
percent = '10 -10 5 -5'.split(' ')

#Result
#1. 순이익을 소수점 첫째자리에서 반올림한 값
#2. 이익인지, 손해인지를 good/same/bad로 나타냄
for i in percent:
    invest *= (1 + int(i)/100)

net = invest - original

print(round(net))

if net > 0 : print('good')
elif net == 0 : print('same')
elif net < 0 : print('bad')
