from functools import reduce
numbers = [40, 60, 80, 120]

double_numbers = list(map(lambda x: x * 2, numbers))
filtered_numbers = list(filter(lambda x: x > 100, double_numbers))
total = reduce(lambda x, y: x + y, filtered_numbers)

print("Original Numbers:", numbers)
print("After Doubling:", double_numbers)
print("After Filtering:", filtered_numbers)
print("Final Sum:", total)