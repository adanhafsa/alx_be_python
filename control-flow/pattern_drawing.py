# Drawing Patterns with Nested Loops

# Prompt the user to input a positive integer that represents the size of the pattern (i.e., the length of each side of the square)
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop for columns (asterisks in each row)
    for _ in range(size):
        print("*", end="")
    print()  # Newline after each row
    row += 1  # Increment row counter