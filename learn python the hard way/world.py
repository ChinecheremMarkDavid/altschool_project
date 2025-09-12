"""
num = int(input("enter number"))
condition = 0
count = 2
iteration = 0


# go throught a number of iterations where the iterations is less than or equal to our initial number


while iteration <= num /2:
    if num % count == 0:
        condition =1
        break
    iteration += 1

if condition == 0:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number ")
"""

names = ["James", "Joseph", "jeremy", "john"]
unique = set()
for name in names:
    if name.islower():
        unique.add(name)
        continue
    unique.add(name.lower())

print(unique)