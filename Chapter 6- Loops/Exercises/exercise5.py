#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
#Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
#and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["Chicken Sandwich", "Tuna Sandwich", "Cheese Sandwich", "Pastrami", "Pastrami", "Pastrami"]  
finished_sandwiches = []


print ("Sorry, the Deli has run out of pastrami...")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

for x in sandwich_orders:   
    finished_sandwiches.append(x)

print(f"New Order: {sandwich_orders}")
print(f"Done: {finished_sandwiches}")