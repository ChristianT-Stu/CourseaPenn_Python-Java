#Prompt the user for thier first name
'''
Using a for loop
    - Print each letter of the name (On the same line)
    - Count each letter in the name
Print the count of the letters in the name
'''

#define user input
name = input("What is your first name? ")

letter_count = 0

print(name, "is spelled:")

#iterate over entered name
for x in name:
    print(x, end = " ")
    letter_count += 1

print('')
print("There are", letter_count, "letters in the name", name)