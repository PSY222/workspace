

def items(list):
    return [i for i in list if i>0] + [i for i in list if i<0]

list = [-1,1,3,-2,2]

print (items(list))
