#test print
word = "Hello"
print(word + " World")

#function: lower() 都轉成小寫
word = "Hello Mr.White"
print(word.lower())
#function: upper() 都轉成大寫
print(word.upper())
#function: islower() 是不是都小寫
print(word.islower())
#function: isupper() 是不是都小寫
print(word.isupper())
#連續做點函式的運算
print(word.lower().islower())

#index
print(word[0])
#find index: .index()
print(word.index("H"))
#如果有找到多個，會回傳最前面那個
print(word.index("l"))

#replace() 替換
print(word.replace("l","L"))

#特殊寫法
s="""Hello

World"""
print(s)
s2="Hello"*3+"world"
print(s2)