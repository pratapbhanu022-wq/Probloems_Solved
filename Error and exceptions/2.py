# this code is only to run in python 2 bcoz in hackerrank input- .*\+
#  .*+ first is true and second is false but in py3 both are correct
import re
t=input() # in py 2 input() by default takes integer
for i in range(t):
    reg=raw_input() # and from raw input takes string in py2 which is incorrect in py3
    try:
        re.compile(reg)
        print(True)
    except re.error:
        print(False)
