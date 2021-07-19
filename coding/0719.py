def happynum(n):
     num = [n]
     while n != 1 or n < pow(10,9):
         k = 0
         for i in str(n):
             k += int(i)**2
         n = k
         num.append(k)
         continue
     return print(num)

def result(n):
    if happynum(n).count(n) >= 2:
           return print("Unhappy Number")
    elif happynum(n).count(n) == 1: return print("Happy Number")


happynum(7)
result(n)

# #
# def happynum(n):
#     list = [n]
#     while n != 1:
#         if len(str(n)) == 1:
#             n = n**2
#             list.append(n)
#             continue
#         elif len(str(n)) == 2:
#             a,b = divmod(n,10)
#             n = a**2 + b**2
#             list.append(n)
#             continue
#         else:
#             times = len(str(n))
#             for i  in range(1,len(str(n))+1):
#                 n %= 10**(times-1)
#             list.append(n)
#             continue
#     return print(list)
#
# happynum(7)
