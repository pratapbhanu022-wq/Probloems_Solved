''' # using pos counter
def merge_the_tools(string, k):
    # your code goes here
    pos = 0
    output = ''
    for x in string:
        if pos == k:
            print(output)
            pos = 0
            output = ''
        if x not in output:
            output += x
        pos += 1
    print(output)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
'''
'''
# one line pythonic solutio using dict.fromkeys
def merge_the_tools(string,k):
    for i in range(0,len(string),k):
        substring= string[i:i+k]
        print(''.join(dict.fromkeys(substring)))
string, k = input(), int(input())
merge_the_tools(string, k)
'''

def merge_the_tools(string,k):
    for i in range(0,len(string),k):
        substring=string[i:i+k]
        output = ''
        for ch in substring:
            if ch not in output:
                output += ch
        print(output)
string, k = input(), int(input())
merge_the_tools(string, k)
