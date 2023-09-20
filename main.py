# Function to count the number of odd numbers among four positive integers
def count_odd_numbers(num1, num2, num3, num4):
    odd_count = 0  # Initialize the count of odd numbers to 0

    # Check each number to see if it's odd
    if num1 % 2 != 0:
        odd_count += 1
    if num2 % 2 != 0:
        odd_count += 1
    if num3 % 2 != 0:
        odd_count += 1
    if num4 % 2 != 0:
        odd_count += 1

    return odd_count

# Input four positive integers
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

# Call the function to count odd numbers
result = count_odd_numbers(num1, num2, num3, num4)

# Output the result
print(result)
