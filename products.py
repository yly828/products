import os

#讀取檔案
def read_file(filename):
    products = [] 
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '名稱,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
        print(products)
    return products


#讓使用者輸入商品名稱與價格
def user_input(products):
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q':
            break
    
        price = input('請輸入商品價格：')
        price = int(price)
        products.append([name, price])
    print(products)   
    return products 

#印出所有商品購買紀錄
def print_products(products):
    for product in products:
        print('商品名稱是', product[0], '價格是', product[1])

#寫入檔案
def write_file(filename,products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('名稱,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')  #str可以用加號合併


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):#檢查檔案在不在
        print('Yes 有這檔案')
        products = read_file(filename)
    else:
        print('找不到檔案....')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()