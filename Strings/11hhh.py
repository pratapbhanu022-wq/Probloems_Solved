def print_rangoli(size): #
    alphabet = [ chr(i) for i in range(97,123)] # letter a sits in 97
    # to 123 total 26 and make a list of all letters

    alphabet = alphabet[:size] # to take to size from start to size
    indices = list(range(size)) # to make the list of given number for eg.
    # if 3 is given than output = [0,1,2]
    indices = indices[:-1] + indices[::-1] # first list here go from
    # last to 0 bcoz -1 will index number will be excluded eg. for size
    # of 3 list would be [0,1] and second list here reverse the 
    # original list which is [2,1,0] so sum of these list make a list=
    # [0,1,2,1,0]
    for i in indices:
        start_index = i+1
        original = alphabet[-start_index:] # - start index to onwards
        # which means for that list [0,1,2,1,0] for i=0 means start_index
        # is 1 and passing that in original in negative would mean 
        # we get 'c' as our first letter and for -2 ='b','c' than
        # -3 a b c than again -2 b c and than -1 so in last -c
        # this is the right side of our rangoli
        reverse = original[::-1] # to make the left side of rangoli just 
        # reverse it so we get c than c b than c b a than c b than c
        row = reverse + original[1:] # here in original we are starting
        # index value 1 bcoz if we start from 0 than last letter of reverse
        # list and first letter of original will be same so after starting
        # from index this would be like
        # c
        # c b c
        # c b a b c
        # c b c
        # c
        row="-".join(row) # to join every letter
        width = size*4-3 # refer index of video to understand
        row = row.center(width,"-") # to centrelize letters and rest of the
        # part will be filled with the - according to width
        print(row)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)