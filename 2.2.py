def count_digits(number):
    number = abs(number)

    if number == 0:
        return 1

    count = 0

    while number > 0:
        number //= 10
        count += 1

    return count

number = int(input(("Enter a number: ")))
print("Total number of digits: ", count_digits(number))
