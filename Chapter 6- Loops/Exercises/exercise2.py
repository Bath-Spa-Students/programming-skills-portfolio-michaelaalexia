#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; 
#if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
#Write a loop in which you ask users their age, and then tell them the cost of their movie ticket

ticket = int(input("Age: "))

while ticket != 0:
    if ticket < 3:
        print("It's free.")
    elif ticket > 12:
        print("It's $15")
    elif ticket >= 3 or ticket <= 12:
        print("It's $10")
    ticket = int(input("Age: "))
print ("Okay, thank you!")