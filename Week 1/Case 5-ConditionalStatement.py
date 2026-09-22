#Example: Python if Statement
number = int(input('Enter a number: '))

# check if number is greater than 0
if number > 0:
    print(f'{number} is a positive number.')

print('A statement outside the if statement.')


# next run
print(" Next Run...")

#Example: Python if…else Statement
number = int(input('Enter a number: '))

if number > 0:
    print('Positive number')
else:
    print('Not a positive number')

print('This statement always executes')


# next run
print(" Next Run...")

number = -5

# Example: Python if…elif…else Statement
if number > 0:
    print('Positive number')

elif number < 0:
    print('Negative number')

else:
    print('Zero')

print('This statement is always executed') 


# next run
print(" Next Run...")


#Python Nested if Statements

number = 5

# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
      print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')


#Compact if Statement
# next run
print(" Next Run...")

number = 10

if number > 0: print('Positive')


#Ternary Operator in Python if...else
grade = 40

result = 'pass' if number >= 50 else 'fail'

print(result)

# next run
print(" Next Run...")

# Logical Operators to Add Multiple Conditions

age = 35
salary = 6000

# add two conditions using and operator
if age >= 30 and salary >= 5000:
    print('Eligible for the premium membership.')
else:
    print('Not eligible for the premium membership') 


# next run
print(" Next Run...")

#Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# next run
print(" Next Run...")
# Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


# next run
print(" Next Run...")

x = 0
y = 5

if x < y:                            # Truthy
    print('yes')

if y < x:                            # Falsy
     print('yes')


if x:                                # Falsy
     print('yes')

if y:                                # Truthy
     print('yes')


if x or y:                           # Truthy
     print('yes')

if x and y:                          # Falsy
     print('yes')


if 'aul' in 'grault':                # Truthy
     print('yes')


if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
     print('yes')


# next run
print(" Next Run...")

# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x


