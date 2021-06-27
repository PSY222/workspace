import fah_converter

print("Enter a celsisus value: "),
celsius = float(input())
fahrenheit = fah_converter.convert_c_tof(celsius)
print('That's '',fahrenheir,'degrees Fahreheit')
