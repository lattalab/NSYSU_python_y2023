import time
b= data= bytes(300000)#An all 0 memory chunk
start = time.time()
while b:
    b = b[1:]
print('bytes:', time.time()-start, "sec")
m = memoryview(data)
start = time.time()
while m:
    m = m[1:]
print('mview:', time.time()-start, "sec")
