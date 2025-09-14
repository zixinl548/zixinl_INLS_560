# Calculate the present value needed to reach a future value

future_value = 30000

# Get user inputs
rate = float(input('Enter the annual interest rate (example: enter 5 for 5%): ')) / 100
years = int(input('Enter the number of years the money will grow: '))

# Calculate present value
present_value = future_value / (1.0 + rate) ** years

# Show result
print('You will need to deposit this amount:', format(present_value, ',.2f'))
