#%%
fruits = ['tomato', 'banana', 'cherry']

print('Fruits:', fruits)
# %%
lst = ['maki', 'terraform', 239, True, {'country': 'nigeria'}, [1, 2, 3]]
print('List:', lst)
print(lst[2])
print(lst[-1][0])
# %%


lst = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(rest)
# %%
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'cherry']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)
print(rest)

# %%
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(rest)
print(tenth)
# %%
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
last_index = len(fruits) -1
fruits[last_index] = 'kiwi'
print(fruits)
# %%
tech = ['html', 'css', 'js', 'python', 'node']
exit = ('python' in tech)
print(exit)
# %%
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)
# %%
list = ['item1', 'item2', 'item3']
list.insert(2, 'new item')
print(list)
# %%
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop(1)
print(fruits)
# %%
items = ['item1', 'item2', 'item3', 'item4']
cpy = items.copy()
print(items)
print(cpy[2])
# %%
list1 = ['item1', 'item2', 'item3']
list2 = ['item4', 'item5', 'item6']
list1.extend(list2)
print(list1)
# %%
positive_numbers = [1, 2, 3, 4, 5]
negative_numbers = [-1, -2, -3, -4, -5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print(negative_numbers)

# %%
numbers = [1, 2, 3, 4, 5, 6, 7,7,7,7,7,7,7,7,7,7, 8, 9, 10]
count = numbers.find(7)
print(count)
# %%
empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0
# %%
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(list))
first_item = list[0]
last_item = list[-1]
middle_item = len(list) // 2

print(first_item, middle_item, last_item)
# %%
mixed_data_types = ['mark-david', 26, 174.2, 'single', 'lagos']

# %%
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(len(it_companies))

it_companies[0] = 'Meta'
print(it_companies)
it_companies.append('Twitter')
print(it_companies)
# %%
first_company = it_companies[0]
last_company = it_companies[-1]
middle_company = it_companies[len(it_companies) // 2]
print(first_company, middle_company, last_company)
it_companies.append('it_company')
print(it_companies)
# %%
it_companies.insert(len(it_companies) // 2, 'new')
print(it_companies)
# %%
str = '# '
print(str.join(it_companies))
# %%
check = 'Apple' in it_companies
print(check)
# %%
it_companies.sort()
print(it_companies)
# %%
it_companies.reverse()
print(it_companies) 
# %%
sliced = it_companies[0:3]
print(sliced)
# %%
last = it_companies[-3:]
print(last)
# %%
middle = it_companies[len(it_companies)//2:]
print(middle)
# %%
it_companies.pop(0)
print(it_companies)
# %%
it_companies.clear()
print(it_companies)
# %%
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)   
# %%
full_stack2 = full_stack.copy()
print(full_stack2)
# %%
full_stack2.pop(-1)
# %%
full_stack2
# %%
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# %%
ages.sort()
print(ages)
# %%
min_age = min(ages)
max_age = max(ages)
middle_age = ages[len(ages) // 2]
avg_age = sum(ages) / len(ages)
range_age = max_age - min_age
print(min_age, max_age, middle_age, avg_age, range_age)
# %%
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
# %%
count1 = count(countries)
print(count1)
# %%
print(count(countries))
# %%
