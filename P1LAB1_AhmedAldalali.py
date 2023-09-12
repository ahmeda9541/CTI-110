# This program calculates and displays travel expenses
# 9/5/2023
# CTI-110 P1HW2 - Travel Expense
# Aldalali Ahmed
#
print('This program calculates and displays travel expenses.\n')
Budget = float(input('Enter Budget here:'))
Destination = input('Enter your Travel Destination :')
Gas = float(input('How much do you think you will spend on gas?'))
Accomodation = float(input('Approximately, how much will you need for accomodation/hotel?'))
Food = float(input('Last, how much do you need for food?'))
print('\n')

print('------------Travel Expenses--------')
print('Location:',Destination)
print('Initial Budget',Budget)
print('\n')

print('Fuel:',Gas)
print('Accomodation:',Accomodation)
print('Food:',Food)

Expenses = Gas + Accomodation + Food
Balance = Budget - Expenses
print('\n')
print('Remaining Balance',Balance)
