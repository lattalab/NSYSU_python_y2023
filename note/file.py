# 檔案物件 = open(檔案路徑 , mode = 開啟模式) ，可以再加encoding選擇要用哪種編碼
#檔案路徑 分  絕對路徑 跟 相對路徑
#another way open file: with open(檔案路徑， mode = 開啟模式) as 檔案物件: ->(會自動關檔)
#一次讀取一行 -> for 變數 in 檔案物件(持續)
#或是   檔案物件.readline() 讀一行
#讀取全部文字 -> 檔案物件.read()
#檔案物件.readlines() 將檔案中的每行資料放到列表
#寫入文字 -> 檔案物件.write(字串)