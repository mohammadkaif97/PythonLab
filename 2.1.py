def reverse_digits(number):
    number_str = str(number)

    for digit in reversed(number_str):
        print(digit, end="")
    print()

number = int(input("Enter an integer: "))

reverse_digits(number)