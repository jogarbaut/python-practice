# Day 5 - Lists

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort() # s
min_age = sorted(ages)[0]
print(f'min_age: {min_age}')

max_age = sorted(ages, reverse=True)[0]
print(f'max_age: {max_age}')

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)

sum_all_ages = 0
age_count = len(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
median = None
mid_index = age_count // 2
if (age_count % 2 == 0):
  # two middle items divided by two
  median = (ages[mid_index] + ages[mid_index - 1]) / 2
else:
  median = ages[mid_index]
print(f'median: {median}')

# Find the average age (sum of all items divided by their number )
for age in ages:
  sum_all_ages += age

print(f'sum of all ages: {sum_all_ages}')
print(f'count of ages: {age_count}')

avg_age = sum_all_ages / age_count
print(f'avg of ages: {avg_age}')

# Find the range of the ages (max minus min)
range = max_age - min_age
print(f'range: {range}')

# Compare the value of (min - average) and (max - average), use abs() method
val_1 = abs(min_age - avg_age)
val_2 = abs(max_age - avg_age)

if val_1 > val_2:
  print('val_1 was larger')
else:
  print('val_2 was larger')
