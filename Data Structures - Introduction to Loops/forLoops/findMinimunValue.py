# Write code that find the minimum value of a list of numbers (5,3,8,-1,-2.2,0)
'''
    - Don't use the built in min() function
    - Instantiate a 'numbers' list variable containing the proper values (above)
    - Iterate over the list and find the min value
    - Print the minimum value in the format: "...is the min number"
'''

#define list of numbers
numbers = [5,3,8,-1,-2.2,0]

#define min number variable
min_number = numbers[0]

#iterate over this list for the min value
for number in numbers:
    #check if the number is less than the defined min num (above)
    if number < min_number:
        #reset min number
        min_number = number

print(min_number, "is the min number.")
