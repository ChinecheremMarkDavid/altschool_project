# %%
a = 3
print('a is positive') if a > 0 else print('a is not')


# %%
a = 0
if a > 0:
    if a % 2 == 0:
        print('a is a positive even number')
    else:
        print('a is an odd number')
elif a == 100:
    print('a is 0')
else:
    print('a is a negative number')
# %%

a = 1
if a > 0 and a % 2 == 0:
    print('a is a positive even number')
elif a > 0 and a % 2 != 0:
    print('a is a positive odd number')
else:
    print('wow')
# %%
member = 'David'
access = 4

if member == 'admin' and access >= 5:
    print('access granted')
else:
    print('access denied')
# %%
age = int(input('enter your age: '))
if age >= 18:
    print('you are old enough to drive')
else:
    print(f'you need {18 - age} more years to learn to drive.')
# %%
mark = int(input('mark enter your age:  '))
stephanie = int(input('stephanie enter your age:  '))
if mark > stephanie:
    print(f'mark you are {mark - stephanie} years older than stephanie')
elif stephanie > mark:
    print(f'stephanie you are {stephanie - mark} years older than mark')
else:
    print('you are the same age')
# %%
student_grade = range(0, 101)
if st