# CTI-110
# P2HW2 - List
# Ahmed
# 9/19/2023
#

#####Pseudocode#####
#lins 12-17 assignment the modules to a variable in the the tabe
#line 20 is the table that is used to get the information from
#line 21 calcultes the Average
#lines 25-28 are the outputs 
Module_1 = float(input('Enter grade for module 1:'))
Module_2 = float(input('Ender grade for module 2:'))
Module_3 = float(input('Enter grade for module 3:'))
Module_4 = float(input('Enter grade for module 4:'))
Module_5 = float(input('Enter grade for module 5:'))
Module_6 = float(input('Enter grade for module 6:'))
print()

my_modules = [Module_1, Module_2, Module_3, Module_4, Module_5, Module_6]
Average = sum(my_modules) / len(my_modules)

print('---------------Results----------------')

print(f'Lowest Grade: {min(my_modules)}')
print(f'Highest Grade: {max(my_modules)}')
print(f'Sum of Grades: {sum(my_modules)}')
print('Average:', f'{Average:.2f}')
print('-----------------------------------------')
