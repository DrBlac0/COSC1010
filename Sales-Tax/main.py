#
# Andres Hunter
# 09-sept-2024
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations



# Constants for the state and county tax rates
st = 0.05
ct = 0.025

# Get the amount of the purchase.
purchase_price = float (input(' Please enter the purchase price of item: '))

# Calculate the state sales tax.
state_sales_tax = purchase_price * st
# Calculate the county sales tax.
county_tax = purchase_price * ct
# Calculate the total tax.
total_tax_price = state_sales_tax + county_tax
# Calculate the total of the sale.
FP = purchase_price + state_sales_tax + county_tax
# Print information about the sale.
print ("The State Sales Tax will be $:", format (state_sales_tax,',.2f'))
print ("The County tax will be $:", format (county_tax,',.2f'))
print ("total tax is $:", format (total_tax_price,',.2f'))
print ("Final Price is $:", format(FP,',.2f'))