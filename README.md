# Description
Coding Project to practice the main topics that I have learned in the Python course at Devops Experts college.
This project has 2 files: decrypt_message.py which is the main program and test_unittests.py which is a unit tests module to test functionality of methods and exceptions in decrypt_message.py file.
The program gets an input text file with encrypted message, decrypts it by switching the most common alphabetical letters and swap them with the most common letters in English (e,t,o,r), appends (add to end of the file) to the input file the decryption and writes to new text file the decryption. Finally, it finds the longest words in the new text file, and appends to the original text file the longest word (first longest word, if it has many words) as the number of lines of the seconds text file (with the decryption only).

# Main topics
collections - list, dictionary, string.
Functions and files manipulating (text files). 
Assertions and exceptions.

# Run
## To run unit tests (unittest build-in package of python) - in CMD:
python -m unittest test_unittests.py
## To run the main program - in CMD:
python -m decrypt_message

