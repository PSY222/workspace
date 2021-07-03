# class Calculator:
#     def __init__(self):
#         self.value = 0
#
#     def add(self,val):
#         self.value += val
#
# class UpgradeCalculator(Calculator):
#     def minus(self,val):
#         self.value -= val
#
# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
# print(cal.value)

# class MaxLimitCalculator():
#     def __init__(self):
#         self.value = 0
#
#     def add(self,val):
#         self.value += val
#         if self.value >= 100: self.value = 100
#
# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(60)
# print(cal.value)

# print(all([1,2,abs(-3)-3]))
# print(chr(ord('a'))=='a')

print(list(filter(lambda x: x>= 0,[1,-2,-5,8,-3])))
print(int('0xea',16))
