requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

# Adding mushrooms
# Adding green peppers
# Adding extra cheese

# Finished making your pizza!

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")
# Adding mushrooms
# Sorry, we are out of green peppers right now.
# Adding extra cheese

# Finished making your pizza!

# Checking That a List Is Not Empty

requested_toppings2 = [] # Empty list
if requested_toppings2:
    for requested_topping in requested_toppings2:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# Are you sure you want a plain pizza?

# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have the {requested_topping}.")

print("\nFinished making your pizza!")
# Adding mushrooms
# Sorry, we don't have the french fries.
# Adding extra cheese

# Finished making your pizza!