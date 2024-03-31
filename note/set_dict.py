#集合的運算
s1={3,4,5}
#in/not in 是否在裡面
print(10 in s1)
print(10 not in s1)
s1={3,4,5}
s2={4,5,6,7}
#s3=s1&s2 交集：取兩個集合中，相同的資料
#s3=s1|s2 # 聯集：取兩個集合中的所有資料，但不重複
#s3=s1-s2 # 差集：從s1中，減去和s2重疊的部分
#s3=s1^s2 # 反交集：取兩個集合中，不重疊的部分
#print(s3)
s=set("hello") #set(字串)
print("h"in s)
print(s)
# 字典的運算
dic={"apple":"蘋果","bug":"害蟲"}
dic["apple"]="小蘋果"
print(dic["apple"])
print("apple" in dic) # define key is there or not
print("appl" not in dic)
print(dic)
del dic["apple"] # 刪除字典中的鍵值對（key-value pair）
print(dic)
dic={x:x*2 for x in [3,4,5]}
print(dic)