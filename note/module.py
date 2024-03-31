# 模組module :獨立的程式檔案
# 將程式寫在一個檔案中，此檔案可重複載入使用

#用法:
#-載入
#import 模組名稱 (as 模組別名)
#-使用
#模組名稱或別名.函式名稱(變數資料)
#模組名稱或別名.變數名稱
import sys
print(sys.platform) #印出作業系統
print(sys.maxsize) #印出整數的最大值
#可以自己建立新模組在import
#建立新的.py檔，在想要使用的程式中import