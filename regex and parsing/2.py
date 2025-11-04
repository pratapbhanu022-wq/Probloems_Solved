import re
reg=r"[,.]"
print("\n".join(re.split(reg,input())))
'''
re.split(reg,string) splits the string whenever the regex matches
join takes a list of string and joins them with "\n" between each.
this means each item will be on a new line.
Ex. ['100','000','000'] will be "100\n000\n000" so this would print each item in
next line
'''