def sum_of_first_10_numbers():
    total_sum = 0

    for num in range (1,11):
        total_sum += num

    return total_sum

result = sum_of_first_10_numbers()
print(f"The sum of the first 10 numbers is :{result}")