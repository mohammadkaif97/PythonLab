def find_numbers_divisible_by5(numbers):
    divisible_by_5 = [num for num in numbers if num % 5 == 0]

    if divisible_by_5:
        print("Numbers divisible by 5 are :")
        for num in divisible_by_5:
            print(num)
    else:
        print("No numbers divisible by 5 were found.")


user_numbers = []
print("Enter 5 numbers :")
for _ in range(5):
    num = int(input())
    user_numbers.append(num)

find_numbers_divisible_by5(user_numbers)
