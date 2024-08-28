def clculate_prouct_and_sum():
    num1 = int(input("Enter the first integer:"))
    num2 = int(input("Enter the second integer: "))

    product = num1*num2

    if product <=5000:
        return f"The product is {product}, which is <=5000, so the sum is {num1+num2}."
    else:
        return f"The product is {product} which is > 5000"

result = clculate_prouct_and_sum()
print((result))