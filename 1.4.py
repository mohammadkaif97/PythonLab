def is_palindrome(number):
    num_str = str(number)

    if num_str == num_str[::-1]:
        return True
    else:
        return False

user_input = int(input("Enter a number"))

if is_palindrome(user_input):
    print(f"{user_input} is a palindrome number.")
else:
    print(f"{user_input} is not a palindrome number.")