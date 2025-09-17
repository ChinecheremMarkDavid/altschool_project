#%%
empty_dict = {}

print(type(empty_dict))
# %%
person = {
    'first_name': "mark",
    'last_name': "david",
    'age': 26,
    'country':'nigeria',
    'is_married': False,
    'skills': ['SQL', 'data engineering', 'python'],
    'address': {
        'street': 'jakande',
        'city': 'lagos',
        'zipcode': '101233'
    }
    
}

print(person['skills'][1])
print(person['country'])
# %%
print(person.get('height'))
# %%
person['job'] = 'data analyst'
# %%
print(person['skills'])
# %%
person['skills'].append('Database administration')
# %%
person['skills'][3] = 'Database administrator'
# %%
print(person['skills'])
# %%


dog = {}
print(type(dog))
# %%
dog['name'] = 'bili'
print(dog)
# %%
dog['colour'] = 'brown'
# %%
dog['breed'] = 'ekuke'
# %%
dog['legs'] = 4
# %%
dog['age'] = 3
# %%
print(dog)
# %%
student = {
    'first_name' : '',
    'last_name' : '',
    'gender' : '',
    'age' : '',
    'marital_status' : '',
    'skills' : [],
    'country' : '',
    'city' : '',
    'address' : {'street' : '', 'zipcode' : '' }
    
}
# %%
print(len(student))
# %%
print(student)
# %%
print (type(student['skills']))
# %%
student['skills'].extend(['HTML', 'CSS', 'JavaScript', 'Python'])
# %%
student
# %%
dict_key_list = list(student.keys())
print(dict_key_list)
# %%
dict_value_list = list(student.values())
# %%
print(dict_value_list)
# %%
studentss = student.items()
print(studentss) 
# %%
del student['age']
# %%
