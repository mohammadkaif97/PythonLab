def print_even_index_characters(s):
    for i in range (0, len(s), 2):
        print(s[i], end=' ')

    print()

input_string = input("Enter s string: ")
print_even_index_characters(input_string)