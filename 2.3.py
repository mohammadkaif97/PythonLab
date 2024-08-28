def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 ==0:
        return False
    i = 5
    while i*i <= number:
        if number % i == 0 or number % (i+2)==0:
            return False
        i +=6

    return True

def display_primes(start , end):
    print(f"Prime numbers between {start} and {end} are:")
    for num in  range(start, end+1):
        if is_prime(num):
            print(num, end='')
        print()

start_range = int(input("Enter the start of the range :"))
end_range = int(input("Enter the end of the range:"))

display_primes(start_range,end_range)


