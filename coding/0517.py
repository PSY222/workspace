a = [41, 43, 45, 47, 49]
for i in a:
    b = []
    c = []
    if i%2 == 1:
        b.append(i)
    elif i%2 == 0:
        c.append(i)

print("홀수 {0}개, 짝수 {1}개".format(len(b),len(c)))
