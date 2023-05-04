#Instructions

'''
Define a function get_factors that takes an integer as a parameter and returns a list of factors of that number.
'''

def get_factors(x):
    '''Returns a list of factors of given number x.'''

    factors = []
    #iterate over range from 1 to number x
    for i in range(1, x + 1):
        #check if i divides number x evenly
        if(x % i == 0):
            factors.append(i)
    return factors

print(get_factors(21))