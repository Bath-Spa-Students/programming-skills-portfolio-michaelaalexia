#A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
#You will to use the arithmetic operators to complete this exercise.

print ("USB STICKS COST £6.\n Note: you have £50.")
quantity = int (input ("How many do you want to buy: "))
price = int(50 - (quantity * 6))
print ("Your change is: \n", price)