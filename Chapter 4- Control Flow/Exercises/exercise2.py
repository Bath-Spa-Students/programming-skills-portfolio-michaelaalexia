#Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#Write one version of this program that runs the if block and another that runs the else block.

alien_color = "red"
ac = input("Alien's Color? ")
if ac == "red":
    print ("5 Points Earned")
else :
    print ("10 Points Earned")

#if block
alien_color = "yellow"
ac = input("Alien Color? ")
if ac == "yellow":
    print ("5 Points Earned")

#else block
alien_color = "green"
ac = input("Alien's Color? ")
if ac == "green":
    print ("10 Points Earned")