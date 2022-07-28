# age = 12
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $25.")
# else:
#     print("Your admission cost is $40.")

# Your admission cost is $25.

# This program can be more efficiently written as:
# age = 12

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65: # You can use as many elif blocks, as needed.
#     price = 40
# else: 
#     price = 20
# print(f"Your admission cost is ${price}.")
# Your admission cost is $25.

# The 'else' block is not required at the end of the if-elif chain.
age = 12

if age < 4:
    price = 0
elif age < 18: 
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")
# Your admission cost is $25.

# 'else' is a catchall and thus a security risk to use. 
# It's far better to specify exact conditions to prevent unusual program behavior due to unforseen user inputs.
