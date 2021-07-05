# n = 5
#
# result = [0,1]
# while 1:
#  temp = result[-1] + result[-2]
#  if temp < n:
#     result.append(temp)
#  else:
#     break
#
# print(result)
#
#
# n = int(input())
#
# result = [0,1]
# while True:
#     temp = result[-2] + result[-1]
#     if temp =< n:
#         result.append(temp)
#     else: break
#
# print(result)

# sumsec = 0
#
# for hour in range(24):
#     for min in range(60):
#         if '3' in str(hour) or '3' in str(min):
#             sumsec += 60
#
# print(sumsec)

#
#   if 3 in a :
#       hour2 = print(sum(hour)*60^3)
#
# for b in min:
#   if 3 in b :
#        min2 = print(sum(min)*60*2)
#
# print(hour2+min2)

# num = int(input())
# car = []
#
# import random
#
# if num>=0:
#     car = random.sample(list,num)
#     print(sum(car),average(car))
#
# clear(car)
#
# sets = 0
#
# def dup():
#     for i in range(10):
#         sets += i
#         return len(set(dup(i))) != len(dup(i))
#
# print("Sample inputs:",dddd)
# print("Sample outputs:",dddd)

n = 6
for a in sorted(range(1,n),reverse=True):
    for b in range(1,n):
        if sum(a,b) = n:
          print("O"*a,"X"*b)
        else: break
