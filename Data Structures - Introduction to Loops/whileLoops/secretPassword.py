#whileLoops Exercise
'''
Write a program that uses while loops to test user input of a secret password.
    - if the user inputs "secret", print "Welcome!" and exit the program
    - Otherwise, print "Sorry, the password you entered is incorrect. Please try again." and prompt the user again.
'''

password = ""
while password != 'secret':

    password = input('Please enter the secret password:')
    if password == 'secret':
        print("Welcome!")
    else:
        print("Sorry, the password you entered is incorrect. Please try again.")