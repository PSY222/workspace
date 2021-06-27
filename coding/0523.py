n = 4

if 0 < n <= 2**32-1 :
    for i in range(1,n+1):
        start = 1
        if n%i == 0:
            start += 1
        else : pass
print(start)
if start%2 == 0: print("yes") #0은 꺼져있음
else: print("no")
