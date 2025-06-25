min = None
for x in range(-10, 11):
    y = 2 * x**2 - 3 * x + 2
    print(f"f({x}) = {y}")
    if(min == None or y < min):
        min = y
print(f"Minimum: {min}")