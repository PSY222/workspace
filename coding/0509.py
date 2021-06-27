# for x in range(10):
#     print('%d: %d'%(x,''.join(map(str, range(1001))).count(str(x))))

# for i in range(10):
#     print('%d: %d'%(i,''.join(map(str,range(1,1001))).count(str(i))))

# print(list(range(10)))
# print(list(map(str, range(10))))
# #
# count = {x:0 for x in range(10)}
#
# for x in range(1,1001):
#     for i in str(x):
#         count[int(i)] += 1
#
# print(count)

# temp = [0]*5
# for i in "1213":
#     temp[int(i)] += 1
#
# print(temp) = [0,2,1,1,0]

# def gop(a,b):
#     for i in list(map(str,list(range(a,b)))):
#         for x in i:
#             temp = []
#             temp.append *= int(x)
#     return print(sum(temp))
#
# gop(10,15))

# def gop(a,b):
#     return eval('+'.join('*'.join(str(x)) for x in range(a,b)))
#
# print(gop(10,16))

# sum=0
# for n in range(10,1001):
#     part=1
#     for i in str(n):
#         part*=int(i)
#     sum+=part
# print(sum)

# for value in gen:
#     print(value)

# for i in "123":
#     print(i)
# #
# a = list(map(str,list(range(1,3))))
# print(a)

# print(list(range(10,16)))

    # for x in :
    #     temp += x*

# def DashInsert(n):
#     n = str()
#     for i in n:
#         new = list(i)
#         if int(i)%2 == 0:
#             new.append("*")
#         elif int(i)%2 != 0:
#             new.append("-")
#     return print(''.join(new))
#
# DashInsert("4546793")

# print(list(map(int,' '.join("4546793").split())))
# a = "4546793"
# print(a.split())


# def complete(N):
#   temp = []
#   for i in range(1,N):
#       for j in range(1,i):
#           if i % j == 0:
#               temp.append(str(j))
#               sum = eval('+'.join(temp))
#       if sum == i:
#           temp.append(str(i))
#   return print(temp)

# complete(28)

# n = int(input())
# print([a for a in range(1,n+1) if a == sum(y for y in range(1,a) if a%y == 0)])
#
# N = int(input("Input a natural number: ")) # 숫자를 하나 입력합니다.
#
# result = [] # 완전수를 저장할 리스트.
#
# for i in range(1, N+1): # 1부터 입력한 숫자까지
#     sum = 0
#     for j in range(1, i): # 1부터 i까지
#         if i%j==0:
#             sum += j # 약수들의 합을 구합니다.
#
#     if i == sum: # 자신을 제외한 약수들의 합이 자신과 같으면, 즉 완전수면..
#         result.append(i)
#
# print(result)

# num= 28
# print([x for x in range(1, num+1) if x==sum(y for y in range(1, x) if x%y==0)])

# def peta(a,b,c):
#     a + b + c == 1000
#     if a^2 + b^2 == c^2:
#         print(a,b,c)
#         print(a*b*c)
#
# map(lambda a,b,c : a*b*c) ????

# for a in range(1,500):
#   for b in range(a,500):
#       c= 1000-a-b
#       if a*a+b*b==c*c:
#           print(a*b*c)
#           print(a,b,c)

# pebo = [1,2]
# [pebo.append(pebo[i-1]+pebo[i]) for i in range(1,4000000) if i%2 == 0 and i <= 4000000]
# print(pebo)
# pebo = [1,2]
# temp = pebo[-1]+pebo[-2]
# while temp % 2 == 0 and temp <= 4000000:
#         pebo.append(temp)
#
# print(sum(pebo))

# i,j=1,2
# sum = 0
#
# while i<4000000:
#     if j % 2 == 0: sum += j
#     i, j = j, i+j
#
# print(sum)


def d(n):
    sum = eval('+'.join(i for i in str(n)))
    return sum + n

print(sum(list(range(1,5001))) - sum([d(i) for i in range(1,5001) if d(i)<=5000]))
