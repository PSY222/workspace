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

#---------------------------------------
# 
# input = list(map(int,'0 15 4 0 7 10 0'.split(' ')))
# 
# for i in range(len(input)):
#     times = 0
#     for j in input:
#         if j >= i:
#             times += 1
#     if times == i:
#         print('h-index:',i)
#         break
# 
# input.sort(reverse = True)
# for i in range(len(input)):
#     if sum(input[0:i]) >= i**2:
#      print('g-index:',i)
#      break

#---------------------------------------

