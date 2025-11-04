# to print 1,2,3,4,5 in same line as it is
'''
for i in range(1,6):
    if i<5:
        print(i,end=",") # print with , till 4 than after 5 no comma
    else:
        print(i)
'''
for i in range(1,4):
    print(f"{i} is squared {i*i}")