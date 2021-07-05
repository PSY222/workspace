S = sorted(list({1,3,4,8,13,17,20}))

def spair(S):
    dict = {}
    for (x, y) in zip(S[:-1], S[1:]):
        if not dict.get(y-x):
            dict[y-x] = [(x,y)]
        else:
            dict[y-x] = dict[y-x] + [(x,y)]

    return dict[min(dict.keys())]

S = [1, 3, 4, 8, 13, 17, 20]
#S = [1,2,4,5,8,15,19]
print(spair(S))


# x = [20]
# for a in S:
#     for b in S:
#         if a > b: a - b
#         elif a < b : b -a
#         else: continue
#             if a-b < min(x):
#              x = []
#              x.append(a)
#              x.append(b)
#             else : continue
# print(x)
