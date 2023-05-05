#Instructions

'''
Create a new script file. Write a program that does the following:
    - Counts the number of vowels in a string.
    - Counts the number of words in a sentence.
'''

def vowel_counter(string):
    ''' Counts the number of vowels in a given string'''

    vowel_count = count_instance_of_str(string, 'aeiou')

    return vowel_count

def word_counter(sentence):
    '''Counts the number of words in a given sentence'''

    sentence = sentence.strip() #removes white space from beginning and end of sentence

    num_spaces = count_instance_of_str(sentence, ' ')

    word_count = num_spaces + 1

    return word_count

def count_instance_of_str(string1, string2):
    '''Count characters in string1 that are also in string 2'''

    count = 0

    #for each chaaracter in string1 check if its in string 2
    for char in string1:
        if char in string2:
            count += 1

    return count

def main():

    while 1 == 1:

        input_string = input('Enter a string: ')

        if input_string == '-1':
            break

        print(vowel_counter(input_string), 'vowels in', input_string)
        #print(word_counter(input_string), 'words in', input_string)

#to execute main function
if __name__ == '__main__':
    main()