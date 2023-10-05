# CTI-110

# P3HW2 - Salary

# Ahmed Aldalali

# 10/5/2023

#

employee_name = input("Enter the name of the employee: ")
hours_worked = float(input("Enter the number of hours worked this week: "))
pay_rate = float(input("Enter the employee's pay rate: "))
print()
# Check if the employee has worked overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

# Calculate the pay for regular hours and overtime pay
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)

# Calculate the gross pay
gross_pay = regular_pay + overtime_pay

print('Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')
print('-------------------------------------------------------------------------------')

print(f'{hours_worked:.2f}', end='         ')
print(f'{pay_rate:.2f}', end='         ')
print(f'{overtime_hours:.2f}',end='       ')
print(f'{overtime_pay:.2f}', end='        ')
print(f'{regular_hours:.2f}', end='        ')
print(f'{gross_pay:.2f}')



