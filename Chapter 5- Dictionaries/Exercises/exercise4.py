#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#Use a loop to print the name of each river included in the dictionary.
#Use a loop to print the name of each country included in the dictionary.

river = {'The Nile' : 'Egypt',
         'The Amazon' : 'South America',
         'The Yangtze' : 'China'}
for key in river:
    print (key, " runs through ", river[key])
for key in river:
    print (key)
print (river['The Nile'], river['The Amazon'], river['The Yangtze'])