# nested dict
students = {
    '101': {'name': 'Alice', 'marks': 88},
    '102': {'name': 'Bob', 'marks': 92}
}
students['102']['marks'] += 5
students['102']['name'] ='bhanu'
print(students) #{'101': {'name': 'Alice', 'marks': 88}, '102': {'name': 'bhanu', 'marks': 97}}