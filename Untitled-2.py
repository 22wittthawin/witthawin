def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)

list_50 = list(range(1, 51))
list_500 = list(range(1, 501))
list_5000 = list(range(1, 5001))

result_50 = sum_of_squares(list_50)
result_500 = sum_of_squares(list_500)
result_5000 = sum_of_squares(list_5000)

print(result_50)
print(result_500)
print(result_5000)
