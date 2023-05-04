#Instructions
'''
Define a function unique_list that takes a list of numbers as a parameter and returns a new list with unique vales.
    - Create a new empty list
    - Use a for loop to iterate over the provided list of numbers
    - Add values to the new list if they don't already exist in the new list
    - Return that new list
'''

def unique_list(l):
    '''Returns a list of unique values from given list l.'''

    new_list = []

    #iterate over provided list
    for i in l:
        #check if number is in new list
        if i not in new_list:
            #add it to new list
            new_list.append(i)

    return new_list

print(unique_list([1,2,3,3,3,3,4,5]))