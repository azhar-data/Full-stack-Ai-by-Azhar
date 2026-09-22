#Python while Loop

number = 1

while number <= 3:
    print(number)
    number = number + 1


# Example: Python while Loop

# Print numbers until the user enters 0
number = int(input('Enter a number: '))

# iterate until the user enters 0
while number != 0:
    print(f'You entered {number}.')
    number = int(input('Enter a number: '))

print('The end.')


#Python while loop with break statementIndentation in Loop

while True:
    user_input = input('Enter your name: ')

    # terminate the loop when user enters end
    if user_input == 'end':
        print(f'The loop is ended')
        break  

    print(f'Hi {user_input}')


#Python while loop with an else clause

counter = 0

while counter  <  2:
    print('This is inside loop')
    counter = counter + 1
else:
    print('This is inside else block')


# Indentation in Loop - know the difference
languages = ['Swift', 'Python', 'Go']

# start of the loop
for lang in languages:
    print(lang)
print('-----')
# end of the for loop

print('Last statement')

#Example: Loop Through a String
language = 'Python'

# iterate over each character in language
for x in language:
    print(x)


#Example: Loop Through a String

    languages = ['Swift', 'Python', 'Go', 'C++']

for lang in languages:
    if lang == 'Go':
        continue
    print(lang)


# iterate from i = 0 to i = 3
for i in range(0, 4):
    print(i)


#The break Statement

    languages = ['Swift', 'Python', 'Go', 'C++']

for lang in languages:
    if lang == 'Go':
        break
    print(lang)


#The continue Statement

    languages = ['Swift', 'Python', 'Go', 'C++']

for lang in languages:
    if lang == 'Go':
        continue
    print(lang)


#Nested for loops

# outer loop 
attributes = ['Electric', 'Fast']
cars = ['Tesla', 'Porsche', 'Mercedes']

for attribute in attributes:
    for car in cars:
        print(attribute, car)
    
    # this statement is outside the inner loop
    print("-----")
    
