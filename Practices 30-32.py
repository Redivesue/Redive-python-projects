# practice 30
temperature_in_celsius = float(input('Enter temperature in celsius: '))
# Convert it to Fahrenheit
temperature_in_fahrenheit = temperature_in_celsius * 1.8 + 32
# Convert it to Kelvin
temperature_in_kelvin = temperature_in_celsius + 273.15
print(f"The temperature in Celsius is {temperature_in_celsius:.2f}, in Fahrenheit is {temperature_in_fahrenheit:.2f} "
      f"and in Kelvins is {temperature_in_kelvin:.2f}" )

# practice 31
pressure_in_kpa = float(input('Enter pressure in kpa: '))
# convert it
pressure_in_psi = pressure_in_kpa * 0.145038
pressure_in_mmHg = pressure_in_kpa * 7.50062
pressure_in_atm = pressure_in_kpa * 0.00986923
print('Pressure in psi: %.2f' % pressure_in_psi)
print('Pressure in mmHg: %.2f' % pressure_in_mmHg)
print('Pressure in atm: %.2f' % pressure_in_atm)

# practice 32
number = int(input('Enter a four-digit integer: '))
the_first_digit = number // 1000
a =number % 1000
the_second_digit = a // 100
b = a % 100
the_third_digit = b // 10
the_fourth_digit = b % 10
print(the_first_digit, the_second_digit, the_third_digit, the_fourth_digit)
print(the_first_digit + the_second_digit + the_third_digit + the_fourth_digit)

