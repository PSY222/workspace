def OneEditApart(a,b):
    count = 0
    if len(a) <= len(b):
     A = [i for i in a]
     B = [j for j in b]
     for i,j in zip(A,B):
         if i == j:count += 1
     if count >= 2: print('true')
     else: print('false')
    elif b in a: print('true')
    else: print('false')
    return

OneEditApart("cat", "dog")
OneEditApart("cat", "cats")
OneEditApart("cat", "cut")
OneEditApart("cat", "cast")
OneEditApart("cat", "at")
OneEditApart("cat", "acts")
