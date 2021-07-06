# def Nmaker(i):
#     for k in range(i):
#         space = 'N'+'N'*i+' '*(i-2)+'N'
#         return print(space)
#
# Nmaker(3)
def NN(n):
    for i in range(n):
        print(''.join(["N" if j in [0,i,n-1] else " " for j in range(n)]))
NN(7)
