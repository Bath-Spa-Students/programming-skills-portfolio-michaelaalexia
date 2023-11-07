#Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 
#move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ["A Sandwich", "B Sandwich", "C Sandwich"]
finished_sandwiches = []

for x in sandwich_orders:
    print (f"Your {x} is ready!")
    finished_sandwiches.append(x)
print (f"Your {finished_sandwiches} has been made.")