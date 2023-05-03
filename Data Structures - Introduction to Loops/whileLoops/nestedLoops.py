#Nested Loops, or loops within loops will have every iteration of the outer loop also run the inner loop iteration as well.

for i in range(1,4):
    print('i:', i) #for each number i
    for j in range(1,3):
        #for each number j
        print('\t', 'j:', j)