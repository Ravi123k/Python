# Get the number of terms for the Fibonacci sequence from the user
num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Initialize the first two terms
first_term = 0
second_term = 1

# Print the first two terms
print(first_term)
print(second_term)

# Loop through the remaining terms and print them
for i in range(num_terms - 2):
    next_term = first_term + second_term
    print(next_term)
    first_term = second_term
    second_term = next_term
