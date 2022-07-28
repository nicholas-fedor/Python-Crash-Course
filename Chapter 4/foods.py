# To copy a list, you can make a slice that includes the entire original list.
# This is done by omitting the index references.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # creates a slice by copying the entirety of the 'my_foods' list.

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Output:
# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake']

# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake']

# We can show that these are two separate lists now, by adding different items to each.
my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods) # ['pizza', 'falafel', 'carrot cake', 'cannoli']
print(friend_foods) # ['pizza', 'falafel', 'carrot cake', 'ice cream']

