import re
import email.utils
for _ in range(int(input())):
    i=input()
    i=email.utils.parseaddr(i)
    if re.match(r"^[a-zA-Z][a-zA-Z0-9\-\_\.]+@[a-z]+\.[a-z]{1,3}$",i[1]):
        print(email.utils.formataddr((i[0],i[1])))