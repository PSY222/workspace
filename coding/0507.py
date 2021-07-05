# def ans(n):
#     return str([i for i in n if i<0]) + str([i for i in n if i>0])
#
# n = [-1, 1, 3, -2, 2]
# print(ans(n))

# starter = [0,1]
#
# def pebo(n):
#     i = 0
#     while (starter[i]+starter[i+1]) <= n:
#         starter.append(starter[i]+starter[i+1])
#         i += 1
#     return(starter)
#
# print(pebo(13))
# -------------------------------------------------------
# n=1000000000
#
# result=[0,1]
#
# while 1:
#     temp = result[-1]+result[-2]
#     if temp < n:
#         result.append(temp)
#     else:
#         break
#
# print(result)

# -----------------------------------------------------
# num = "0123456789 01234 01234567890 6789012345 012322456789"
# num1 = num.split(' ')
# print(num1)
# print(len(num1))
#
# i = 0
# for i in range(9):
#     i += 1
#     if len(num1[i]) != len(set(num1[i])):
#         True
#     else:
#         False
#
# [i for i in range(9) ]

print(list(map(lambda n:len(n) == 10,"0123456789 01234 01234567890 6789012345 012322456789".split())))
