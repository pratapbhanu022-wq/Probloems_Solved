'''
#1. By default every print fn print output in new line. to print in same line we use end=""
print('hello',end="") # sep="" will not work in this bcz it only works for one print statement
print('world') 
# output = helloworld
'''
'''
#2. to print without space between items sep=" "
print('hello','world', sep=" ") # output = hello world --without sep output =helloworld
'''
'''
#3. Concatenating strings without using +
name='Bhanu'
print("hello", name) # using this space is automatically given
print("Hello " + name) # in first string space is given
'''
'''
#4. Printing variables
x=4
print(f'value of x is {x}') # using f string formatting
print('value of x is' ,x)
'''
'''
#5. Printing special characters
print('hello, "world"')
print('hello\nworld') # out after \n would be in new line 
# also \ is used to print special characters
'''
