import json
from data import data
from nested_dictionary import nested_data

'''
DICTIONARY
This function will check a dictionary for lists.
For each key in the dictionary -> if the value to the key is a list ->
check each item within the list for the selected name ->
if the name is found return the list name and the found name.
'''
# Find a name by searching through all lists within the dictionary:
def find_name(dict, name):
    results = {}
    for key, value in dict.items():
        if isinstance(value, list):
            matches = [item for item in value if item == name]
            if matches:
                results[key] = matches
                
    return results

'''
NESTED DICTIONARY
The following function will go from outer to inner to value to find the "path" to to a specific name.
dat -> outer group -> check if inner group is a dictionary -> if the value in the inner is a list
-> check each item in the list if they match the name -> if name is present in the items in the list
-> return the results of the search
'''
def find_names_nest(data, name):
    results = {}
    for outer, inner in data.items():
        if isinstance(inner, dict):
            for inner, value in inner.items():
                if isinstance(value, list):
                    matches = [item for item in value if item == name]
                    if matches:
                        results.setdefault(outer, {})[inner] = matches
    if results:
        return results
    else:
        return f"{name} was not found in the data."