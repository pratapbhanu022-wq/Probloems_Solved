def minion_game(string):
    Vowels ='AEIOU'
    Stuart_s=Kevin_s=0
    lenght=len(string)
    for i in range(lenght):
        if string[i] in Vowels:
            Kevin_s+=lenght-i
        else:
            Stuart_s+=lenght-i
    if Kevin_s>Stuart_s:
        print(f"kevin {Kevin_s}")
    elif Stuart_s>Kevin_s:
        print(f"stuart {Stuart_s}")
    else:
        print('Draw')
s = input()
minion_game(s)
    