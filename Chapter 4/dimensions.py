dimensions = (200, 50)
print(dimensions[0]) # 200
print(dimensions[1]) # 50

# dimensions[0] = 250 - Doesn't work - cannot modify a tuple.

# Looping Through All Values in a Tuple
for dimension in dimensions:
    print(dimension) 
    # 200
    # 50

dimensions = (400,100)
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)
    # Modified Dimensions:
    # 400
    # 100

