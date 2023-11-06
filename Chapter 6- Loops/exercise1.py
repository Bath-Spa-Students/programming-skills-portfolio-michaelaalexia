## Exercise 1: Pizza Toppings :ballot_box_with_check:

##Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

##print a message saying you’ll add that topping to their pizza.

expected_response = "quit"
response = input()
while response != expected_response{
    print(f"Topping:{response}")
}