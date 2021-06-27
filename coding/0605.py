# def convert(n, base):
#     T = "0123456789ABCDEF"
#     q, r = divmod(n, base)
#     if q == 0:
#         return T[r]
#     else:
#         return convert(q, base) + T[r]

def repeat(n):
    counts = {}
    new = []
    j = 0
    for i in range(len(n)+1):
        if n[i] == n[i+1]:
            j += 1
        else: break
    j += 1
    counts[n[i]] = j
    return print(counts)

def next(n):
    N = [i for i in n]
    for i in range(len(n)+1):
        if n[i] == n[i+1]:
            N.remove(n[i])
    n = ''.join(N)
    return repeat(n)

next('aaabbcccccca')
