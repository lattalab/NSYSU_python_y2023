# Iterable 資料型態
# 字串、列表、集合、字典

# for 迴圈
# for 變數名稱 in 可疊代的資料:
print("String:")
for x in "abc":
    print(x,end=", ")
print();print()

print("Set:")
for x in {"a","test",1,10}:
    print(x,end = ", ")
print();print()

print("List:")
for x in [1,2,3,4]:
    print(x, end = ",")
print();print()

print("Dictionary:")
for x in {'a':3, "x":5}: # 先看key
    print(x, end = ",")
print();print()

# 內建函式
# max(可疊代資料)
# sorted(可疊代資料)
print("Built-in functions: ")
print(max({1,2,3,4}))
print(max({'a':3, "x":5}))

# sorted 會回傳list
print(sorted("abc"))
print(sorted([5,121,22,8,1]))