def sum_of_digits(number):
    total_sum = 0

    number = abs(number)

    while number > 0:
        digit = number % 10
        total_sum += digit
        number //= 10

    return total_sum

user_input = int(input("Enter an integer: "))

result = sum_of_digits(user_input)
print(f"The sum of digits of {user_input} is : {result}")
