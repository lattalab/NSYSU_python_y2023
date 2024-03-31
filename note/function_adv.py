#參數的預設資料
def power(base,exp=0):
    print(base**exp)
power(2,3)  #base = 2 , exp = 3
power(4)    #base = 4 , exp = 0

print()
#使用參數名稱對應
def divide(n1,n2):
    print(n1/n2)
divide(2,4)
divide(n2 =2, n1 =4)

print()
#無限參數資料
# :無限參數以 tuple 資料形態處理
#呼叫函式，可傳入無限數量的參數
def average(*ns):
    print(ns,type(ns))
    sum = 0
    for n in ns:
        sum+=n
    print(sum/len(ns))
average(3,4)
average(3,5,10)
average(1,4,-1,-8)