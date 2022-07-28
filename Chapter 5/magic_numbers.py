answer = 17
if answer != 42:
    print(f"{answer} is not the correct answer. Please try again!")
    # 17 is not the correct answer. Please try again!

# Conditional statements
age = 19
print(age < 21) # True
print(age <= 21) # True
print(age > 21) # False
print(age >= 21) # False

# Using 'and' to Check Multiple Conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) # False
age_1 = 22 # changes value of age_1 to '22'
print(age_0 >= 21 and age_1 >= 21) # True

# Using 'or' to Check Multiple Conditions
age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >= 21) # True

age_0 = 18
print(age_0 >= 21 or age_1 >= 21) #False 

# Checking Whether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings) # True
print('pepperoni' in requested_toppings) # False