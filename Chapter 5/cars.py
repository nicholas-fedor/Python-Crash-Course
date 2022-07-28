cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper()) # Capitalizes all of 'bmw'
    else:
        print(car.title()) # Capitalizes the first letter of the other cars not matching 'bmw'.

    # Audi
    # BMW
    # Subaru
    # Toyota

car = 'bmw' # sets the variable 'car' to equal the string 'bmw'
result = (car == 'bmw') # checks if the variable 'car' has a value of 'bmw' and the variable 'result' stores the output.
print(result) # true

result2 = (car == 'audi')
print(result2) # False

# Ignoring Case When Checking for Equality
car2 = 'Audi'
print(car2 == 'audi') # False

# If case matters, then you can convert the string to lowercase before the comparison.
print(car2.lower() =='audi') # True

# Note that lower() doesn't change the value that was originally stored.
car3 = 'Ford'
print(car3.lower() == 'ford') # True
print(car3) # Ford