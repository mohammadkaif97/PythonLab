def factorial(number):
    result = 1

    for i in range (1, number + 1):
        result *= i
    return result

user_input = int(input("Enter a number :"))

if user_input < 0 :
    print("Factorial is not definedfor negative numbers")
else:
    result = factorial(user_input)
    print(f"The factorial of {user_input} is : {result}")