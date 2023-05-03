#Write a program that asks the user for numbers (ints). It computes the average of the numbers.
#Allow the user to enter -1 to quit the program.

num_list = []
initial_count = 0
playing = True

while (playing == True):
    num = int(input('Enter an int:'))
    #test if number is -1 to quit the program
    if (num == -1):
        playing = False
    else:
        #add numbers to list of numbers
        num_list.append(num)
        initial_count += 1

#get the sum of all entered numbers
num_sum = 0
for num in num_list:
    num_sum += num

#calculate the average
num_avg = num_sum / initial_count

print('avg:', num_avg)
