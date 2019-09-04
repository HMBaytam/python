# declare variable
types_of_people = 10
# declare x to be a string with formating
x = f'There are {types_of_people} types of people.'

# declare string as variable
binary = 'binary'
# declare string as variable
do_not = "don't"
# declare a formated string as variable
y = f'Those who know {binary} and those you {do_not}'

# print x - it will be formatted
print(x)
# print y - it will be formatted
print(y)

# print string with formatting
print(f'I said: {x}')
# print string with formatting
print(f'I also said: {y}')

# declare bool as a variable
hilarious = False
# declare string with empty formatting brackets as a variable
joke_evaluation = "Isn't the joke so funny?! {}"

# print previous variable with a function to input hilarious in the empty formatting brackets
print(joke_evaluation.format(hilarious))

# declare a string as a variable
w = 'This is the left side of...'
# declare a string as a variable
e = 'a string with a right side'

# concatonate variable w with variable e
print(w+e)
