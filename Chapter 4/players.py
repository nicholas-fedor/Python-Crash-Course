# Slices - A specific group of items in a list

# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # ['charles', 'martina', 'michael']

# if you wanted the second, third, and forth items
print(players[1:4]) # ['martina', 'michael', 'florence']

# if you omit the first index reference, then the first element of list is used.
print(players[:3]) # ['charles', 'martina', 'michael']

# vice versa if the slice's end reference is missing.
print(players[2:]) # ['michael', 'florence', 'eli']

# prints the last three players and will continue as the list changes.
print(players[-3:]) # ['michael', 'florence', 'eli']

# a third reference when creating a slice will reflect how many items to skip.
print(players[0:4:2]) # ['charles', 'michael']

# Looping throug a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    # Here are the first three players on my team:
    # Charles
    # Martina
    # Michael

