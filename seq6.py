# Problem 1: Bottle Deposits


# In many towns a small deposit is added to drink containers to encourage people to recycle
# them. In one particular town, drink containers holding one liter or less have a Rs 5.00
# deposit, and drink containers holding more than one litre have a Rs 7.50 deposit.
# Write a program that reads the number of containers of each size from the user. Your
# program should continue by computing and displaying the refund that will be received for
# returning those containers.
# Format the output so that it includes a dollar sign and two digits to the right of the decimal
# point.


# Input the number of small and large containers
small_containers = int(input("Enter the number of containers holding 1 liter or less: "))
large_containers = int(input("Enter the number of containers holding more than 1 liter: "))

# Define deposit values
small_deposit = 5.00  # Rs 5.00 for small containers
large_deposit = 7.50  # Rs 7.50 for large containers

# Calculate the total refund
total_refund = (small_containers * small_deposit) + (large_containers * large_deposit)

# Display the refund amount formatted with a currency symbol
print(f"Your total refund amount is: Rs {total_refund:.2f}")
