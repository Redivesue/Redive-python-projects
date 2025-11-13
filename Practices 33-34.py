# practice 33
integer1 = int(input('Enter the first number: '))
integer2 = int(input('Enter the second number: '))
integer3 = int(input('Enter the third number: '))

integer_max = max(integer1, integer2, integer3)
integer_min = min(integer1, integer2, integer3)
integer_mid = (integer1 + integer2 + integer3) - integer_max - integer_min

print(f"Descending order :{integer_max, integer_mid, integer_min}")

# practice 34
current_bread_quantity = int(input('the current bread quantity: '))
old_bread_quantity = int(input('old bread quantity: '))
current_price = 3.49
old_price = 3.49 * 0.6
print(f"Current bread price:{current_price:.2f}")
print(f"Old bread price:{old_price:.2f}")
print(f"Total bread price:{current_price * current_bread_quantity + old_price * old_bread_quantity:.2f}")