#Write a python program that takes courses marks as input and then calculates average of all the courses. 
#After calculating the average, calculate the percentage of a student using total marks. 
#Assume the total of all the courses marks is 500 or take the total marks from the user as input.

code_lab_mark = int(input("Enter your Code Lab Marks: "))
digital_storytelling_mark = int(input("Enter your Digital Storytelling Marks: "))
digital_vis_design_mark = int(input("Enter your Digital Visual Design Marks: "))
a = int(code_lab_mark + digital_storytelling_mark + digital_vis_design_mark)
average = int(a/3)
print ("Your average is: ", average)
p = (average/100)
percentage = (p*100)
print ("Your percentage is: ", percentage)