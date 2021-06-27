def convert_c_to_f(celsius_value):
    return celsius_value*9.0/5+32

for i in range(10):
    try:
        print(i,10//i)
    except ZeroDivisionError as err:
        print(err)
        print("Not divided by 0")
    else:
        print(10/i)

string_ex = 'abc123abc'
for value in string_ex:
    try:
        value.isdigit()
    except ValueError as err:
        print(err)

While True:
 value = input('변환할 정수값을 입력해주세요')
  for digit in value:
      if digit not in '0123456789':
          raise ValueError("숫자값을 입력하지 않으셨습니다")
  print("정수값변환 숫자")
