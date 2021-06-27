print("구구단을 몇단을 계산할까요?")
a = int(input())
print(a)
print("구구단",a,"단을 계산합니다.")
for i in range(1,10):
    print(a,"*",i,"=",a*i)
    i += 1
