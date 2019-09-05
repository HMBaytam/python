# imports argv from the sys module
from sys import argv

# expands argv into the script and filename variables
script, filename = argv

# opens the filename
txt = open(filename)

# prints the string
print(f'Here\'s your file {filename}: ')
# prints the text in the file
print(txt.read())

# prints the strinf
print('Type filename again:')
# asks user for an input
file_again = input('>')

# opens the second file
txt_again = open(file_again)

# prints the text in the second file
print(txt_again.read())
