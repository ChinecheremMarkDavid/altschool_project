
my_age = 26
my_height = 174.2


base = int(input("what is the base?"))
height = int(input("what is the height?"))
area = 0.5 * base * height

print(f"the area of the triangle is {area}")


#%%
side_a = int(input("what is side a"))
side_b = int(input("what is side b"))
side_c = int(input("what is side c"))
perimeter = side_a + side_b + side_c
print(f"the perimeter of the triangle is {perimeter}")

# %%

lenght = int(input("what is the lenght?"))
width = int(input("what is the width?"))
area = lenght * width
perimeter = 2 * (lenght + width)

print(area)
print(perimeter)
# %%



#%%
py = print(len("python"))
dr = print(len("dragon"))
print(len(py) == len(dr))


# %%
print("on" in "python" and "on" in "dragon")
# %%
print("jargon" in "i hope this cousrse is not full of jargon")
# %%
lenght = str((len("python")))

print(lenght)
print(type(lenght))
# %%
even_number = 10
odd_number = 9

print(odd_number % 2 == 0)
# %%
floor = 7 // 3
intr = int(2.7)

print(floor)
print(floor == intr)
# %%
ten = "10"
Ten = 10

print(type(ten) == type(Ten))
# %%

print(int('9.8') == 10)
# %%
hours = int(input("enter hours:"))
work_rate = int(input("enter work rate:"))
pay = hours * work_rate
print(f"your weekly earning is {pay}")
# %%
number_of_years = int(input("enter number of years:"))
seconds = number_of_years * 365 * 24 * 60 * 60
print(f"the number of seconds you lived is {seconds}")
# %%
for i in range(1, 6):
    print(i, i**0, i**1, i**2, i**3, i**4, i**5)
# %%
