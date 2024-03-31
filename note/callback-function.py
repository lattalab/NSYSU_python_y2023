def test(arg):
    arg() # 呼叫回呼函式

# 定義一個回呼函式
def handle():
    print(100)

# 定義另一個回呼函式(有參數)
def handle2(da):
    print(da)

def test2(arg):
    arg(1000) # 呼叫回呼函式


# 範例
def add(n1 , n2 ,funcs):
    funcs(n1+n2)

def result(R):
    print("結果是: ",R)

test(handle)
test2(handle2)
add(3, 4, result)