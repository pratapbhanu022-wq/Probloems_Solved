# flatten a nested dict/convert a dict into a single level dict
data={'a':10,'b':{'x':15,'y':{'z':25}}}
flat={}
def flatten(d,parent_key=''): # parent_key: a string representing the prefix for nested keys.
    # Default is an empty string.
    for k,v in d.items():
        key=f"{parent_key}.{k}" if parent_key else k
        if isinstance(v,dict): # to check if value is a nested dict or not if yes than recursion
            flatten(v,key)
        else:
            flat[key]=v
flatten(data)
print(flat)
# out= {'a': 10, 'b.x': 15, 'b.y.z': 25}


'''
pip install flatten_json before using it
from flatten_json import flatten
flattened_dict = flatten(data, separator='_')

'''