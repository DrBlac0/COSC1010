#
# Andres Hunter     
# 15/Sept/2024
# Hot Dog Cookout Calculator Programming Project
# COSC 2409 DNT

#Constants
hot_dogs_per_package = 10
hot_dogs_buns_package = 8

#Variables
hot_dogs_needed = int  
people = int
people_per_share = int

#inputs
people = int(input("Enter the number of people attending the cookout: "))
hot_dogs = int(input("Enter the number of hot dogs each person will eat: "))    

#Calculations of  hot dogs and buns needed
hot_dogs_needed = people * hot_dogs

if hot_dogs % hot_dogs_per_package == 0:
        hot_dog_packages = hot_dogs_needed // hot_dogs_per_package
else:
        hot_dog_packages = hot_dogs_needed // hot_dogs_per_package + 1

if hot_dogs % hot_dogs_buns_package == 0:
        hot_dogs_buns = hot_dogs_needed // hot_dogs_buns_package
else:
        hot_dogs_buns = hot_dogs_needed // hot_dogs_buns_package + 1

#print the calculations
print ("The minimum number of hot dogs required is: ", hot_dogs_per_package)
print ("The minimum number of hot dog buns packages required is: ", hot_dogs_buns)

#leftovers
hot_dogs_leftovers = hot_dog_packages * hot_dogs_per_package - hot_dogs
hot_dogs_buns_leftovers = hot_dogs_buns * hot_dogs_buns_package - hot_dogs_needed

print (" The left over hotdogs will be: ", hot_dogs_leftovers)
print (" The left over hotdog buns will be: ", hot_dogs_buns_leftovers)

# Use comments liberally throughout the program. 