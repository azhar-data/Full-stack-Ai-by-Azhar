# Create a new set:
print("Create a new set:")

# Initialize an empty set and assign it to the variable 'x':
x = set()

# Print the empty set 'x':
print(x)

# Print the data type of 'x', which should be 'set':
print(type(x))

# Print a newline for separation:
print("\nCreate a non-empty set:")

# Create a non-empty set 'n' with the elements 0, 1, 2, 3, and 4 using a set literal:
n = set([0, 1, 2, 3, 4])

# Print the non-empty set 'n':
print(n)

# Print the data type of 'n', which should be 'set':
print(type(n))

# Print a newline for separation:
print("\nUsing a literal:")

# Create a set 'a' using a set literal with elements 1, 2, 3, 'foo', and 'bar':
a = {1, 2, 3, 'foo', 'bar'}

# Print the data type of 'a', which should be 'set':
print(type(a))

# Print the set 'a':
print(a)




myset = {"apple", "banana", "cherry"}
print ( myset)




# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)




# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = { }

# check data type of empty_set
print('Data type of empty_set:', type(empty_set))

# check data type of dictionary_set
print('Data type of empty_dictionary:', type(empty_dictionary))



numbers = {21, 34, 54, 12}

print('Initial Set:',numbers)

# using add() method
numbers.add(32)

print('Updated Set:', numbers) 



companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

# using update() method
companies.update(tech_companies)

print(companies)

# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}



languages = {'Swift', 'Java', 'Python'}

print('Initial Set:',languages)

# remove 'Java' from a set
removedValue = languages.discard('Java')

print('Set after remove():', languages)