# This program calculates and displays travel expenses
# 9/7/2023
# CTI-110 P1HW2 - Travel Expense
# Aldalali Ahmed
#
######### Pseudocode ################
#
#What the user need's to fill up
print('This program calculates and displays travel expenses.\n')

# Convert user input to float
Budget = float(input('Enter Budget here: '))

Destination = input('Enter your Travel Destination: ')

Gas = float(input('How much do you think you will spend on gas? '))

Accommodation = float(input('Approximately, how much will you need for accommodation/hotel? '))

Food = float(input('Last, how much do you need for food? '))
print('\n')

# Where the user is going and what is the Budget
print('------------Travel Expenses--------')
print('Location:', Destination)
print('Initial Budget: $', Budget)
print('\n')

# The Expenses
print('Fuel: $', Gas)
print('Accommodation: $', Accommodation)
print('Food: $', Food)

# The math / result
Expenses = Gas + Accommodation + Food
Balance = Budget - Expenses

print('\n')
print('Remaining Balance: $', Balance)
