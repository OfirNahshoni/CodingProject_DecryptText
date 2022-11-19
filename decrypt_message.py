# Project 1 Python Course (Devops experts)
# The purpose of this project is to practice the knowledge I have so far with course material:
# Strings, Operators, Loops, Nested loops, Conditions, Lists, Dictionaries, Files manipulation, Functions, Exceptions, Assertions, unit tests.
# This project decrypts a message from a given text file (which is encrypted),
# appends the encryption to the original file and writes it to a new text file.
# Finally, the program finds the longest words in the second text file (with the decryption only)
# and appends the (first) longest word into the original text file as the number of lines in the second file.
# re package is for regular expressions to find patterns in a string - finds the alphabetical letters in a word.
# Unit Tests - there are 2 options to run the unit tests I wrote:
# Run the file test_unittests.py from the IDE or
# Write in CMD (make sure you are on thee right directory): python -m unittest test_unittests.py


# Imports - Packages, Libraries, Modules
import re


# Constants
ENC_MSG_FILENAME1 = 'message1.txt'
ENC_MSG_FILENAME2 = 'message2.txt'
ENC_MSG_FILENAME3 = 'message3.txt'


# Helpers
def readTxtFile(filepath):
    # Helper function to all program - read all content of text file into a single string and returns it
    message = ''
    # Read the text file
    with open(filepath, 'r') as file:
        message = file.read() # Returns a string
    return message


def frequencesDict(_str):
    # Helper function to Part 1
    mydict = {}
    for char in _str:
        # If char is a letter in English
        if char.isalpha():
            if ord(char) >= 65 and ord(char) <= 90:
                # Check if a Capital letter
                occurences = mydict.get(char.lower(), 0)
                occurences += 1
                mydict[char.lower()] = occurences
            else:
                # If a lower case letter
                occurences = mydict.get(char, 0)
                occurences += 1
                mydict[char] = occurences
    return mydict


def findMostCommonLetterInList(_list):
    # Helper function to Part 1
    # Function that finds most common letter in a list of tuples (char, frequences)
    # Add an exception on the type of _list ????
    max_val = 0
    for key,value in _list:
        # Add exceptions on the type of key and value ????
        if value > max_val:
            max_val = value
            max_key = key
    return max_key, max_val


# Part 1 - Dictionary of 4 most common letters in the encrypted message
def replaceCommonOccurences(_str):
    freq_dict = frequencesDict(_str) # Dict with frequences of English letters in the string
    print(f'Frequences dictionary:\n{freq_dict}')
    items_list = [x for x in freq_dict.items()] # List of tuples (key, value)
    replaced_dict = {} # Output dictionary

    # Find the most common letter
    most_common = findMostCommonLetterInList(items_list) # Tuple = (max_key, max_val)
    # Remove max tuple from items_list
    del items_list[items_list.index(most_common)]
    # Add to output dict
    replaced_dict[most_common[0].lower()] = 'e'
    replaced_dict['e'] = most_common[0].lower()

    # Find the second most common letter
    most_common = findMostCommonLetterInList(items_list) # Tuple = (max_key, max_val)
    # Remove max tuple from items_list
    del items_list[items_list.index(most_common)]
    # Add to output dict
    replaced_dict[most_common[0].lower()] = 't'
    replaced_dict['t'] = most_common[0].lower()

    # Find the third most common letter
    most_common = findMostCommonLetterInList(items_list) # Tuple = (max_key, max_val)
    # Remove max tuple from items_list
    del items_list[items_list.index(most_common)]
    # Add to output dict
    replaced_dict[most_common[0].lower()] = 'o'
    replaced_dict['o'] = most_common[0].lower()

    # Find the fourth most common letter
    most_common = findMostCommonLetterInList(items_list) # Tuple = (max_key, max_val)
    # Remove max tuple from items_list
    del items_list[items_list.index(most_common)]
    # Add to output dict
    replaced_dict[most_common[0].lower()] = 'r'
    replaced_dict['r'] = most_common[0].lower()

    return replaced_dict


# Part 2 - Decrypte a string according to replaced_dict from Part 1
def replaceCharsInText(text_to_change):
    replaced_dict = replaceCommonOccurences(text_to_change) # Dictionary of chars to replace
    print(f'Replaced dictionary:\n{replaced_dict}')
    replaced_chars_list = [key for key in replaced_dict.keys()] # List of keys
    changed_text = '' # Outpute string

    # Iterate through the given string
    for i in range(len(text_to_change)):
        current_char = text_to_change[i]
        if current_char in replaced_chars_list or current_char.lower() in replaced_chars_list:
            # Replace char with the value from replaced_dict
            changed_text += replaced_dict[current_char.lower()]
        else:
            # Copy the char from the given string
            changed_text += text_to_change[i]

    return changed_text


# Part 3 - Decrypt message from message.txt, append the decryption to message.txt and create results.txt with the decryption
def decode_text(filepath, resultpath):
    encrypted_msg = readTxtFile(filepath) # String original message
    decrypted_msg = replaceCharsInText(encrypted_msg) # String changed message

    # Append decryption to original file
    with open(filepath, 'a') as file:
        file.write(f'\nThe decryption for the above text is:\n{decrypted_msg}')
        print('The decryption has been added to decrypt_message.txt successfully')

    # Create another file only with the decryption
    with open(resultpath, 'w') as file:
        file.write(decrypted_msg)
        print('File results.txt has been created successfully')


# Part 4 - Two functions: one to find the longest words in results.txt and second to count the number of lines in results.txt
def longestWordsInFile(filepath):
    # First function that finds and returns the longest words in a file
    txt = readTxtFile(filepath) # String input
    words = txt.split() # Output list
    new_txt = '' # New String - Only alphabetical letters
    regex = re.compile('[^a-zA-Z]') # Regular expression of lower case or upper case letters
    alpha_str = '' # Alphabetical string

    # Iterate through words in list
    for i in range(len(words)):
        word = words[i]
        # Iterate through chars in word
        for char in word:
            alpha_str += regex.sub('', char)
        words[i] = alpha_str # Set words to alphabetical chars only
        alpha_str = '' # Reset the alphabetical string
    
    # Find the longest words in list - with another list of lengths
    lengths = [len(word) for word in words]
    max_words_len = max(lengths)
    
    # Throw away all the words, except the ones that have maximum length
    words = [word for word in words if max_words_len == len(word)]

    return words

def numOfLines(filepath):
    # Returns an integer - number of lines in a text file
    with open(filepath, 'r') as file:
        return len(file.readlines())

def appendLongestWordToFile(filepath, word, amount = 0):
    # Append to a text file the string 'word', 'amount' times
    with open(filepath, 'a') as file:
        file.write('\n')
        for i in range(amount):
            file.write(word + ' ')
        print('Longest word has been added to original file successfully')


# Main process
if __name__ == '__main__':
    # Inputs
    text_to_change1 = "///bha Taa3add, bha Tdaer, enr b7ha Fdcccccbbb..."
    text_to_change2 = "///bha Taa3add, bha Td,aer enr b7ha Fdcccccbbb.\n abdhfgcvry.."
    text_to_change3 = "sdf/// adsvndjnfjnjfder bha\n Taa3add, bha Tdajndjn\nfjnjfder, enr Tdajtuynfjnjfder b7ha Fdcccccbbb..."


    # Write each input into a text file
    with open(ENC_MSG_FILENAME1, 'w') as file:
        file.write(text_to_change1)
    with open(ENC_MSG_FILENAME2, 'w') as file:
        file.write(text_to_change2)
    with open(ENC_MSG_FILENAME3, 'w') as file:
        file.write(text_to_change3)
    

    # Results - Parts 3 & 4
    print('-------------------------- Result 1 --------------------------')
    decode_text(ENC_MSG_FILENAME1, 'result1.txt')
    longest_words = longestWordsInFile('result1.txt')
    print(f"Longest words are:\n{longest_words}")
    num_of_lines = numOfLines('result1.txt')
    appendLongestWordToFile(ENC_MSG_FILENAME1, longest_words[0], num_of_lines)
    print('--------------------------------------------------------------\n')

    print('-------------------------- Result 2 --------------------------')
    decode_text(ENC_MSG_FILENAME2, 'result2.txt')
    longest_words = longestWordsInFile('result2.txt')
    print(f"Longest words are:\n{longest_words}")
    num_of_lines = numOfLines('result2.txt')
    appendLongestWordToFile(ENC_MSG_FILENAME2, longest_words[0], num_of_lines)
    print('--------------------------------------------------------------\n')

    print('-------------------------- Result 3 --------------------------')
    decode_text(ENC_MSG_FILENAME3, 'result3.txt')
    longest_words = longestWordsInFile('result3.txt')
    print(f"Longest words are:\n{longest_words}")
    num_of_lines = numOfLines('result3.txt')
    appendLongestWordToFile(ENC_MSG_FILENAME3, longest_words[0], num_of_lines)
    print('--------------------------------------------------------------\n')

    
    '''
    
    # For Debugging!!
    # Results - Part 1
    # encrypted_txt = readTxtFile(DEC_MSG_FILENAME)
    # replaced_dict = replaceCommonOccurences(encrypted_txt)
    # print(f'Replaced dictionary:\n{replaced_dict}')

    # Results - Part 2
    # print(f'Encrypted sentence:\n{text_to_change}')
    # changed_text = replaceCharsInText(text_to_change)
    # print(f'Decrypted sentence:\n{changed_text}')

    '''
    