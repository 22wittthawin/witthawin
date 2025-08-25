def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total

my_list = [50, 500, 5000]

result = sum_of_squares(my_list)
print("ผลบวกกำลังสอง =", result)
