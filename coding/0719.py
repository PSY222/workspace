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

#making CamelCase to Pothole_case!

def location(n):
    location  = []
    for i in n:
        if i.isupper() == True or i.isdigit() == True:
            location.append(i)
        else: pass
    return location
#
def separate(n):
    n2 = [i for i in n.lower()]
    id = []
    t = 0
    for i in location(n):
        id.append(n.index(i))
    for loc in id:
        n2.insert(loc+t,'_')
        t += 1
    return print(''.join(n2))


separate('numGoat30')
