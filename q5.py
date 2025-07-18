def check_divisibility(num, divisor):
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return "Both inputs must be numeric"
    
    return num % divisor == 0


# Task 2
scenario1 = check_divisibility(10,2)
scenario2 = check_divisibility(7,3)
print (scenario1)
print (scenario2)
