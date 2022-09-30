products = []
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


# print(products[0][0])
# print(products[0][1])

for product in products:
	print('商品名稱是', product[0], '價格是', product[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('名稱' + ',' + '價格' + '\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  #str可以用加號合併



