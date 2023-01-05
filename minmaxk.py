# 2. Python – Maximum and Minimum K elements in Tuple

tup = (5, 20, 3, 7, 6, 8)
k = 2
res = []
test_tup = list(sorted(tup))
test_tup = list(test_tup)
temp = sorted(test_tup)
res = tuple(temp[:k] + temp[-k:])
print(res)