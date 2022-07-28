# A list is a collection of items in a particular order.
# Good to name list variables in their plaural form, i.e. books vs book.
# Square brackets [] indicates a list.

from pickle import TRUE


bicycles = ['trek', 'cannondale', 'redline']

print(bicycles) # ['trek', 'cannondale', 'redline']

# each item on a list can be accessed by its index reference number, starting with zero.
print(bicycles[0]) # trek

# can also apply string methods
print(bicycles[0].title()) # Trek

# using negative reference numbers (i.e. -1) allows you to access items from the end of the list more efficiently.
# i.e. -1 = last item on the list, -2 is second from last, etc
print(bicycles[-1].title()) # Redline

# Using Individual Values from a List
message = f"My first bicycle was a {bicycles[0].title()}."
print(message) # My first bicycle was a Trek.

# Changing, Adding, and Removing Elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'
print(motorcycles) # ['ducati', 'yamaha', 'suzuki']

# Appending Elements to the End of a List
motorcycles.append('harley')
print(motorcycles) # ['ducati', 'yamaha', 'suzuki', 'harley']

# Appending Elements to an Empty List
birds = []
birds.append('robin')
birds.append('blue jay')
birds.append('sparrow')
print(birds) # ['robin', 'blue jay', 'sparrow']

# Inserting Elements into a List
birds.insert(0,'eagle') # adds 'eagle' to the beginning of the list.
print(birds) # ['eagle', 'robin', 'blue jay', 'sparrow']

# Removing Elements from a List
# Using the del Statement
colors = ['red', 'green', 'blue', 'yellow']
print(colors) # ['red', 'green', 'blue', 'yellow']
del colors[3]
print(colors) # ['red', 'green', 'blue']

# Using the pop() Method
# The pop() method removes the last item in a list, 
# but lets you work with that item after removing it.
music = ['rock', 'pop', 'blues']
print(music) # ['rock', 'pop', 'blues']

popped_music = music.pop()
print(popped_music) # blues
print(music) # ['rock', 'pop'] ... note that 'blues' has been removed.

print(f"I really enjoy {popped_music.title()}.") # I really enjoy Blues.

# Popping Items from any Position in a List
first_favorite_music = music.pop(0)
print(f"{first_favorite_music.title()} was my first favorite type of music.") # Rock was my first favorite type of music.

# Removing an item by value.
bad_food = ['soda', 'candy', 'cake']
bad_food.remove('candy')
print(bad_food) # ['soda', 'cake']

# Organizing a List
# Sorting in Alphabetical Order
cars = ['bmw', 'audi', 'subaru']
cars.sort()
print(cars) # ['audi', 'bmw', 'subaru']

# Sorting in Reverse Alphabetical Order
cars.sort(reverse=True)
print(cars) # ['subaru', 'bmw', 'audi']

# Finding the Length of a List
print(len(cars)) # 3