#Lambda is an anonymous function(nameless function) where we can write a code in single line
'''
greater = lambda a,b:a if a>b else b

print(greater(12,13))
print(greater(50,70))
print(greater(40,20))
print(greater(16,26))

wish=lambda name: f'Welcome to the course {name}'

print(wish("Sri"))
print(wish("Elohim"))
print(wish("Divya"))

even = lambda n: 'Even' if n%2==0 else 'Odd'

print(even(7))
print(even(98))
print(even(47))

avg = lambda a,b,c: (a+b+c)/3

print(avg(2,7,9))
print(avg(45,89,90))
print(avg(45,34,32))
'''
'''
domain = lambda mail: (mail.split('@')[-1]).split('.')[0]

print(domain('divya@codegnan.com'))
print(domain('divya@gmail.com'))
print(domain('divya@outllok.com'))
print(domain('divya@yahoo.com'))
'''
'''
gst = lambda price: price + price*0.18

print(gst(1000))
print(gst(3000))
print(gst(8000))
'''
'''
prices = [3992,3929,939202,3023,2323]
res = list(map(lambda price: price + price*0.18, prices))
print(res)
'''
'''
names = ['Elohim','Adonai','yahweh','yeshua']
res = list(map(lambda name: name.title(), names))
print(res)
'''
prices = {3992,3929,939202,3023,2323}
res = list(map(lambda price: price-price*0.3, prices))
print(res)