x=999
y=99

palindrome = []
for n in range(x,y,-1):
    for i in range(x,y,-1):
        product = n*i
        product_str = str(product)
        if product_str[0]==product_str[-1] and product_str[1]==product_str[-2] and product_str[2]==product_str[-3]:
            palindrome.append(product)
print(max(palindrome))