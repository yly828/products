#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '名稱,價格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

#讓使用者輸入商品名稱與價格
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
    	break
    
    price = input('請輸入商品價格：')
    price = int(price)
    # p = [name, price]
    # p=[]
    # p.append(name)
    # p.append(price)
    products.append([name, price])
print(products)	

#印出所有商品購買紀錄
for product in products:
	print('商品名稱是', product[0], '價格是', product[1])

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('名稱,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  #str可以用加號合併



