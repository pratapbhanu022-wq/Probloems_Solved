'''
Tuple of Functions
Problem:
Store multiple lambda functions inside a tuple and apply each to an input.
'''
funcs = (lambda x: x + 1, lambda x: x**2, lambda x: x % 2)
for f in funcs:
    print(f(5))
'''
6
25
1
'''
