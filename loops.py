# LOOPS

'''
  - ITERATRE over a SEQUENCE (e.g. list, tuple, dictionary, set, string)
  - does not require an indexing variable
  - break statement included; stops the loop before it has looped completely
  - continue statement included; stop the current iteration of a loop and 'continue' to the next
  - range() function; sets the number of times the code loops
  - else keyword to execute code after loop is finished
'''

# for loop
thislist = ['apple', 'banana', 'cherry']
for x in thislist:
  print(x)

# range()
for x in range(6):  # range of numbers from 0 to 5 --> (0, 1, 2, 3, 4, 5)
  print(x)

for x in range(1, 7):
  print(x)  # 1, 2, 3, 4, 5, 6

# else keyword is a block of code that will execute after a loop is finished
  ''' will not be executed if loop is stopped by a break statement '''
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# nested loops - inner loop is executed one time for each iteration of the outer loop
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for x in adj:
  for y in fruits:
    print(x, y)

# loop through index numbers
  ''' use range() and len() functions to create iterable '''
thislist = ['apple', 'banana', 'cherry']
for i in range(len(thislist)):
  print(thislist[i], '   index', i)

# WHILE loop
  ''' use len() to determine length of the list and after each item, increment the index by 1 '''
thislist = ['apple', 'banana', 'cherry']
i = 0
while i < len(thislist):
  print(thislist[i], 'index = {}'.format(i))
  i += 1
else:
  print('While loop finished')