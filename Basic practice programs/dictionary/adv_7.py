# short a dict by value in descending order
sales = {'Mon': 200, 'Tue': 450, 'Wed': 150, 'Thu': 300}
sorted_sales = dict(sorted(sales.items(), key=lambda x: x[1], reverse=True))
print(sorted_sales)