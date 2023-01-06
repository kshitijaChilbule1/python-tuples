# 13. Counts the number of occurrences of item 50 from a tuple

count = 0
tuple1 = (50, 10, 60, 70, 50)

for i in tuple1:
    if i == 50:
        count += 1
print(count)