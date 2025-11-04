def print_full_name(first, last):
    s=f"Hello {first} {last}! You just delved into python."
    #return s
    print(s) # prints the string but return none


first_name = input()
last_name = input()
print(print_full_name(first_name,last_name))