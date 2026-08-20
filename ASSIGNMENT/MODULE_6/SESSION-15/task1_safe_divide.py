def safe_divide(a, b):

    try:
        
        result = a / b
        return result

    except ZeroDivisionError:
       
        return "Cannot divide by zero"

print(safe_divide(10, 2))
print(safe_divide(10, 0))