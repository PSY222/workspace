# n = 3
#
# def min(n):
#     if 0 <= n <= 10000 and n%2 != 0 and n%5 != 0:
#         for i in range(1,10**n):
#             a = i*n
#             if (a-1):
#                      break
#                 else: continue
#     else: print("None")
#     return print(a)
#
# min(n)

def a(n):
    b = '1'
    while int(b) % n != 0: b += '1'
    return len(b)
print(a(7))
x = '1'+'1'
print(type(x))
print(len('121'))
