#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
#Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#Print a message to each of the two people still on your list, letting them know they’re still invited.
#Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

invitees = ["JoJo", "LaLa", "YanYan", "DanDan", "TanTan"]
invitees[4] = "VenVen"
print ("Hey! ", invitees[0], " wanna come with me to dinner? My place at 7? Let me know when you can come or not!")
print ("Hey! ", invitees[1], " wanna come with me to dinner? My place at 7? Let me know when you can come or not!")
print ("Hey! ", invitees[2], " wanna come with me to dinner? My place at 7? Let me know when you can come or not!")
print ("Hey! ", invitees[3], " wanna come with me to dinner? My place at 7? Let me know when you can come or not!")
print ("Hey! ", invitees[4], " wanna come with me to dinner? My place at 7? Let me know when you can come or not!")
print ("Hey everyone! Unfortunately considering the place and time, only two people could make it to dinner this week, however we can invite everyone else together some other day!")
invitees.pop()
invitees.pop()
invitees.pop()
print ("Hey VenVen! I'm afraid there won't be space in my place for dinner this week...don't worry though! We can arrange something next week.")
print ("Hey DanDan! I'm afraid there won't be space in my place for dinner this week...don't worry though! We can arrange something next week.")
print ("Hey YanYan! I'm afraid there won't be space in my place for dinner this week...don't worry though! We can arrange something next week.")
print ("Hi ", invitees[0], " are we still down for dinner this week? Let me know when you can come.")
print ("Hi ", invitees[1], " are we still down for dinner this week? Let me know when you can come.")