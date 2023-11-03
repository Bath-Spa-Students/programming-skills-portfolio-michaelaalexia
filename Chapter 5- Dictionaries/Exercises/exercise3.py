#Now that you know how to loop through a dictionary,
#clean up the code from Exercise 6-3 (page 99) by replacing your series of 
#print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add file more Python terms 
#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

dictionary = {'variable' : 'name representing value stored in computer memory', 
              'data types' : 'they categorize value in memory',
              'integers' : 'data types involving numbers without decimal point',
              'float' : 'data types involving numbers with decimal point',
              'strings' : 'data types involving words and letters'}
for key in dictionary:
    print (key, "-->", dictionary[key])