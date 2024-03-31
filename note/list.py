#列表list
scores = [90,70,60,50,80]
friend = ["小黑","小白","小綠"]
thing = [90,"小黑",True]
print(thing)
#取值
print(scores[0]) #從左開始第幾位
print(scores[-2]) #從右往前開始第幾位
print(scores[1:4]) #從第一位開始取到第四位(但不包含第四位)
print(scores[1:]) #從第一個開始 取到結束
print(scores[:4]) #從第四個以前的東西(不包含第四位)

phase = "Hello , Mr.White" #similiar
print(phase[0:5])

#改值
#scores[0]= 30 
#extend 增廣
#You can merge one list into another by using extend() method.
#scores.extend(friend) = [90,70,60,50,80,"小黑","小白","小綠"]

#append 增加
#scores.append(30) = [90,70,60,50,80, 30]
#insert 加到指定位置
#scores.insert(2,30) = [90,70,  ,30,  60,50,80]
#remove 
#scores.remove(90) =[70,60,50,80]
#clear 清空
#scores.clear() =[]
#pop() 移除最後一個，裡面可指定要刪的index
#del 刪除對應index的元素
#del scores[-1] =[90,70,60,50]
#scores.pop() =[90,70,60,50]
#sort() 小到大排列
scores.sort()
print(scores)
#reverse() 反轉
scores.reverse() 
print(scores)
#index() 找位置，有重複會回傳最前面那個
print(scores.index(90))
#count() 告訴有幾個在裡面
print(scores.count(90))
#len() 長度
print(len(scores))
#列表串接
#scores=scores+[12,33] =[90,70,60,50,80,12,33]