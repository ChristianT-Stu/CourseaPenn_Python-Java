#Instructions
'''
Let's define a function greater_than
    - It takes two numbers as parameters
    - It returns True if the 1st parameter is greater that the 2nd parameter
'''

def greater_than(x, y):
    if x > y:
        return True
    else:
        return False

result = greater_than(12,9)
print(result)