# Aldalali Ahmed
#10/2/2023
#CTI 110


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1:'))
mod_2 = float(input('Enter grade for Module 2:'))
mod_3 = float(input('Enter grade for Module 3:'))
mod_4 = float(input('Enter grade for Module 4:'))
mod_5 = float(input('Enter grade for Module 5:'))
mod_6 = float(input('Enter grade for Module 6:'))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
Average = sum / len(grades)

# Results
print('---------------Results-----------------')
print('Lowest Grade:', f'{low:.2f}')
print('Highest Grade:', f'{high:.2f}')
print('sum of Grades:', f'{sum:.2f}')
print('Average:', f'{Average:.2f}')
print('-------------------------------------------------')
# determine letter grade for average
if Average >= 90:
    print('Your grade is: A')
else:
    if Average >= 80:
        print('Your grade is: B')
    else:
        if Average >= 70:
            print('Your grade is: C')
        else:
            if Average >= 60:
                print('Your grade is: D') 
            else:
                 if Average <= 59:
                     print('Your grade is: F')
        
               




