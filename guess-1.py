# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話 要告訴他 比答案大小

import random
key = random.randint(1, 100)
count = 0
while 1:
	count += 1
	num = input('請猜數字: ')
	num = int(num)
	print('這是你猜的第', count, '次')
	if num == key:
		print('終於猜對了!')
		break
	elif num > key:
		print('比答案大')
	else:
		print('比答案小')