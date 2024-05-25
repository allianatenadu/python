print('Please enter the following:')
# print() creates a blank line
print()
Adjective = input('adjective:')
Animal = input('animal:')
Verb_1 = input('verb:')
Exclamation = input('exclamation:')
Verb_2 = input('verb:')
Verb_3 = input('verb:')
# This time I used a \n to mak the blank line before this:
print('\nYour story is:')
# print() creates a blank line
print()
print('The other day, I was really in trouble. It all started when I saw a very')
# I used double due to exclamation
print(f'{Adjective.lower()} {Animal.lower()} {Verb_1.lower()} down the hallway. "{Exclamation.capitalize()}!" I yelled.But all')
print(f'I could think to do was to {Verb_2.lower()} over and over. Miraculously,')
print(f'that ccaused it to stop, but not befoere it tired to {Verb_3.lower()}')
print('right in front of my family.')