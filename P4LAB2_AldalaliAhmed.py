
first_integer = int(input())
second_integer = int(input())

if second_integer < first_integer:
    print("Second integer can't be less than the first.")
else:
    while first_integer <= second_integer:
        print(first_integer, end=" ")
        first_integer += 5

    print() 
