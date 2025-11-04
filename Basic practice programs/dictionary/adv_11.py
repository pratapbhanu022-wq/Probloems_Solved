# find top 3 highest occuring elements in a dict
from collections import Counter
data = {'apple': 10, 'banana': 25, 'cherry': 15, 'mango': 20}
top3 = dict(Counter(data).most_common(3))
print(top3)