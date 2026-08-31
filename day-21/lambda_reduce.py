from functools import reduce
# reduce is used to combine a single line of code
'''
l =[3992,3929,939202,3023,2323]
res = reduce(lambda sum, i:sum+i,l)
print(res)
'''
'''
names = ['Elohim','Adonai','yahweh','yeshua','Elshaddai']
res= reduce(lambda res,i:res+' '+i, names)
print(res)
'''
products = {
    'sugar':60,
    'salt':50,
    'eggs':90,
    'cooking oil':120,
    'bread':45
}
print(dict(sorted(products.items())))
print(dict(sorted(products.items(),reverse=True)))
print(dict(sorted(products.items(),key=lambda i:i[1])))
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))