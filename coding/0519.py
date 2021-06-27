x = 12.5
if x.isalpha() == True:
    print("math error")
elif x.isdigit() == True:
    if x - int(x) == 0: print("정수입니다")
    elif  x - int(x) != 0: print("소수입니다")
