#control structure : logical design controlling order of statements
#decision structure : check condition
#be careful regarding indentation - no curly braces in Python in if statement
#assignment operator = used for assigning value

tickets = float(input("How many tickets do you wanna buy: "))
price = 10
if tickets > 50 :
    price = 500
else: 
    price = 10
print ("Your tickets cost: "+str(price))

temperature = float(input("What is the temperature today? "))
if temperature < 40: 
    print ("It's a little chilly, isn't it?")
else:
    print ("Nice weather isn't it?")