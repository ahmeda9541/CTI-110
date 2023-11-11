# Pseudocode for P4HW2 - Calculate Gross Pay for Multiple Employees

# Initialize variables to keep track of totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
total_employees = 0

# Start an infinite loop to continue entering employee information
while True:
    # Ask the user for the employee's name or "Done" to terminate
    employee_name = input("Enter the name of the employee (or 'Done' to terminate): ")

    # Check if the user wants to terminate the program
    if employee_name == 'Done':
        break

    # Increment the total number of employees
    total_employees += 1

    # Ask the user for the number of hours worked and the pay rate for the current employee
    hours_worked = float(input("Enter the number of hours worked this week: "))
    pay_rate = float(input("Enter the employee's pay rate: "))

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

    # Calculate the gross pay for the current employee
    gross_pay = regular_pay + overtime_pay

    # Add the current employee's pay to the respective totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    # Display the pay details for the current employee
    print('Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')
    print('-------------------------------------------------------------------------------')
    print(f'{hours_worked:.2f}', end='         ')
    print(f'{pay_rate:.2f}', end='         ')
    print(f'{overtime_hours:.2f}', end='       ')
    print(f'{overtime_pay:.2f}', end='        ')
    print(f'{regular_hours:.2f}', end='        ')
    print(f'{gross_pay:.2f}')

# Display the totals for all employees
print("\nTotal Overtime Pay:", total_overtime_pay)
print("Total Regular Pay:", total_regular_pay)
print("Total Gross Pay:", total_gross_pay)
print("Total Number of Employees Entered:", total_employees)
