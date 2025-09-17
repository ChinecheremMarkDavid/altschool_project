#%%
st = {'item1', 'item2', 'item3', 'item4', 'item5'}
print(st)
# %%
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)
# %%
print(len(fruits))
# %%
print('mango' in fruits)
print(fruits)
# %%
fruits.add('kiwi')
# %%
print(fruits)
# %%
fruits.update(['apple', 'grape'])


# %%

st1 = {'item1', 'item2', 'item3'}
st2 = {'item3', 'item4', 'item5'}
st3 = st1.intersection(st2)
print(st3)
# %%
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

# %%
it_companies.add('twitter')
print(it_companies)
# %%
it_companies.update(['LinkedIn', 'Snapchat'])
print(it_companies)
# %%
it_companies.pop()
print(it_companies)
# %%
it_companies.remove('Apple')
print(it_companies)
# %%
a = {19, 22, 24, 20, 25, 26, 80}
b = {19, 22, 20, 25, 26, 24, 28, 27, 66,44, 22}
c = a.union(b)
print(c)
# %%
print(a.intersection(b))
# %%
print(a.issubset(b))
# %%
print(a.isdisjoint(b))
# %%
print(a.symmetric_difference(b))

# %%
del c
# %%
print(c)
# %%
ages = [22, 19, 24, 25, 26, 24, 25, 24]

set_ages = set(ages)
print(set_ages)
print(type(set_ages))
# %%
print(len(ages))
print(len(set_ages))
# %%
sentence = 'I am a teacher and I love to inspire and teach people'
set_sentence = set(sentence.split())
print(set_sentence)
# %%
print(len(set_sentence))
# %%
