#%%
brothers = ('John', 'Michael', 'David')
sisters = ('Sarah', 'Jessica', 'Emily')
siblings = brothers + sisters
print(siblings)

# %%
len(siblings)
# %%
parents = ('Robert', 'Linda')
family_members = siblings + parents
print(family_members)
# %%
family_members
# %%
fruits = ('apple', 'banana', 'cherry', 'date')
vegetables = ('carrot', 'broccoli', 'spinach', 'potato')
animal_products = ('milk', 'cheese', 'yogurt', 'butter')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
# %%
food_stuff_lt = list(food_stuff_tp)
# %%
print(food_stuff_lt)
# %%
slice_middle = food_stuff_lt[len(food_stuff_lt) // 2:]
# %%
print(slice_middle)
# %%
mi = food_stuff_tp(len(food_stuff_tp) // 2[:])
print(food_stuff_tp)
print(mi)
# %%
first = food_stuff_lt[0:3]
last = food_stuff_lt[-3:]
print(food_stuff_lt)
print(first, last)
# %%
del food_stuff_tp
# %%
