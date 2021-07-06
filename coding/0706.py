# def Nmaker(i):
#     for k in range(i):
#         space = 'N'+'N'*i+' '*(i-2)+'N'
#         return print(space)
#
# Nmaker(3)
# def Nmaker(n):
#     for i in range(n):
#      print(''.join(["N" if j in [0,i,n-1] else " " for j in range(n)]))
#
# Nmaker(7)

# print((150+70+65)/(6+10))
#
# def gasungbi(num):
#     a = 10 #원래 기계의 가격
#     aa = 150 #원래 기계의 성:
#     extraP = 3
#     extra = [30,70,15,40,65]
#     num = len(extra)
#     l = []
#     for m in extra: #추가를 하나만 할때
#         l.append((aa+m)/(3+10))
#          #추가를 2개 할때
#
# extra = [30,70,15,40,65]
# print([i for i in extra])

a = 10 #원래 기계의 가격
aa = 150 #원래 기계의 성:
extraP = 3
extra = [30,70,15,40,65]
extra.sort(reverse=True)
n = 0
k = {}
for i in extra:
    n += 1
    m = (aa+i)//(3*n+a)
    k[i] = m
    aa += i

print(max(k.values()))
