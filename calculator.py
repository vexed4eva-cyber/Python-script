"""
This program asks the user for three ingredients,
three amounts, and a number of servings, and
determines how much of each ingredient is needed
to serve the specified number of servings.
"""

# Write program here...
i1 = input("enter first ingreditent: ")
i1n = float(input("how much of ingredient?: "))
i2 =input("enter next ingredient: ")
i2n = float(input("how much of ingredient?: "))
i3 = input("Enter third ingredient: ")
i3n = float(input("How much of ingredient?: "))
servings =int(input("how many servings?: "))
total_1 = (i1n * servings)
total_2 = (i2n * servings)
total_3 = (i3n * servings)
print(f"total ounces of {i1} {total_1}")
print(f"total ounces of {i2} {total_2}")
print(f"total ounces of {i3} {total_3}")