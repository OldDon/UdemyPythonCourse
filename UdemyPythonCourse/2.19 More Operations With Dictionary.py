person97 = {"name":"Jack", "surname":"Smith", "age":"29"}
person97.pop("name")
'Jack'
person97
{'surname': 'Smith', 'age': '29'}
person97["name":"Jack"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'slice'
person97["name"]="Jack"
person97
{'surname': 'Smith', 'age': '29', 'name': 'Jack'}
person97["age"]="30"
person97
{'surname': 'Smith', 'age': '30', 'name': 'Jack'}
keys = ["a", "b", "c"]
values = [1,2,3]
keys
['a', 'b', 'c']
va
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'va' is not defined
values
[1, 2, 3]
mydict = dict(zip(keys, values))
mydict
{'a': 1, 'b': 2, 'c': 3}

