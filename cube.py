# 3. Create a list of tuples from given list having number and its cube in each tuple

list = [1, 2, 3]

res = [(i, pow(i, 3)) for i in list]

print(res)