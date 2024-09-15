#
# Andres Hunter
# 15/Sept/2024
# Areas of Rectangles Programming Project
# COSC 2409 DNT
#
# Local variables
length1 = int
width1 = int
length2 = int
width2 = int



# Get length A
length1 = int(input( "Please enter the length of rectangle 1: "))

# Get width A
width1 = int(input( "Please enter the width of rectangle 1: "))

# Get length B
length2 = int(input( "Please enter the length of rectangle 2: "))

# Get width B
width2 = int(input( "Please enter the width of rectangle 2: "))

# Calculate area A
area1 = length1 * width1

# Calculate area B
area2 = length2 * width2

# Print area comparison using if-elif-else statements
if area1 > area2:
    print("The area of rectangle 1 is greater than the area of rectangle 2.")
elif area1 < area2:
    print("The area of rectangle 1 is less than the area of rectangle 2.")
else:
    print("The area of rectangle 1 is equal to the area of rectangle 2.")
    