#%%
print("coding" + " " + "for" + " " + "all")
# %%
var = "company"
print(len(var))
# %%
print(var.upper())
# %%
print(var.lower())
# %%
print(var.swapcase())
# %%
word = "coding for all"
print(word[0])
# %%
word = "coding for all"
print(word.find("animal"))
# %%
"coding for all people".replace("coding", "python")
# %%
"python for everyone".replace("everyone", "all")
# %%
"coding for all".split()
# %%
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(',')
# %%
"coding for all".rfind('i')
# %%
'You cannot end a sentence with because because because is a conjunction'.index(because)
# %%
sentence = 'You cannot end a sentence with because because because is a conjunction'
first = sentence.find('because')
last = sentence.rfind('because') + len('because')

result = sentence[first:last]
print(result)
# %%
'   Coding For All      '.strip()
# %%
print('thirty_days_of_python'.isidentifier())
# %%
print('i am enjoying this challenge. \n i just wonder what is next')
# %%
print('name\tage\tcountry\tcountry\nmark\t200\tamerica\tflorida')
# %%
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
# %%
