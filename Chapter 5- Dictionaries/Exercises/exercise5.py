#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and theowner’s name. 
#Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet

dog = {'pomeranian' : 'Jenna',
       'shih-tzu' : 'Grayson',
       'husky' : 'Kyle'} 
cat = {'persian cat' : 'Katie'}
bird = {'budgie' : 'Phil',
        'parrot' : 'Dani'}
pets = (cat, dog, bird)
for key in pets:
    print(key)