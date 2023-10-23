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

#double

temperature = float(input("What is the temperature today? "))
if temperature < 40: 
    print ("It's a little chilly, isn't it?")
else:
    print ("Nice weather isn't it?")

#ascii 
str1 = "Mark"
str2 = "Marie"
str2 > str1
print ("str2 is bigger than str1")


#nested decision
earning = int(input("Enter your earning per month: "))
experience = float(input("How long have you been in this field: "))
if earning > 4000:
    if experience >=2:
        print ("You are elegible for this task.")
    else:
     print ("I'm afraid you are going to need more time.")
else: 
  print ("Your earning is 4000.")
