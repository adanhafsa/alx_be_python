# Multiplication Table

# Prompt the user to input a number for which they want to see the multiplication table
number = int(input("Enter a number to see its multiplication table:"))

# Generate and print the multiplication table by using a for loop
for i in range (1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")

