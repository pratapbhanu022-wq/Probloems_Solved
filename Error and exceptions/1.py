t=int(input())
result=[]
for _ in range(t):
    a,b=input().split()
    try:
        
        result.append(str(int(a)//int(b)))
    except ZeroDivisionError:
        result.append('Error Code: integer division or modulo by zero')
    except ValueError:
        result.append("Error Code: invalid literal for int() with base 10:\n'$'")
for r in result:
    print(r)
'''
# Hackerrank accepted
t=int(input())
result=[]
for _ in range(t):
    a,b=input().split()
    try:
        
        result.append(str(int(a)//int(b)))
    except Exception as e:
        result.append('Error Code: '+ str(e))
    
for r in result:
    print(r)

'''