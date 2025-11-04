def count_substring(string, sub_string):
    count=0
    for i in range(len(string)-len(sub_string)+1): # for the example 
       # ABCDCDC i=5 this i this us how many possible starting position
       # we can check for a substring of length 3 inside a string
       # of length of 7
       if string[i:i+len(sub_string)]==sub_string: # HERE we are comparing 
         # sliced part of string with sub to check if they are equal
         # for eg. if i=0 than it will compare [0:3]=sub which means
         # ABC=CDC or not than i=1 than [1:4]=cdc means BCD=CDC flase
         # and so on till i =4 bcoz [4:7]==CDC true and main string is 
         # also only index till 7= ABCDCDC this example is taken from
         # hackerrank
         count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)