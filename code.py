# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.62138i

# calculate mile
miles = kilometers * conv_fac
print('%0.22f kilometers is equal to %0.2f miles' %(kilometers,miles))

