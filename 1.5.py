def calculate_cubes(n):

    cubes = {i : i**3 for i in range (1, n+1)}
    return cubes

upper_limit = int(input("Enter a number: "))

cubes_dict = calculate_cubes(upper_limit)
print("Cubes of numbers from 1 to",{upper_limit},":")
for number , cube in cubes_dict.items():
    print(f"{number}^3 = {cube}")