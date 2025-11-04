# find top 3 value in a dict
scores={'bhanu':85,'abhi':89,'alok':99,'ravi':79}
top3=sorted(scores.items(),key=lambda x:x[1],reverse=True)[:3]
print(top3) # [('alok', 99), ('abhi', 89), ('bhanu', 85)]