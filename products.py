products = []
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
    	break
    
    price = input('請輸入商品價格：')
    p = [name, price]
    # p=[]
    # p.append(name)
    # p.append(price)
    products.append(p)
print(products)	

print(products[0][0])
print(products[0][1])

