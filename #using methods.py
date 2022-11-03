#using methods
mycolors = ['red', 'blue'] #the list of strings

mycolors.append('black') #using method of append to add new item to list.

print ('this is my first print', mycolors)

mycolors.insert(1, 'purple') #using insert we can also decide location of the added value, for example location 1.

print('this is my 2nd print', mycolors)

mycolors.reverse()  #using reverse to print the list backwards.
print('this is my last print', mycolors)

#mycolors.clear()
#print('Another method with my son Arya', mycolors)
mycolors.extend(('white', 'yellow', 'zebra')) #extend will add multiple values to list.
mycolors.sort()
print('This is your list sorted out', mycolors)
