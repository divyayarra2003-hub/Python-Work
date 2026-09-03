
'''
s = 'Python Programming'
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        print(i,s[i])
        '''

'''
l = [23,45,12,34,50,24,35,68,75,34,10]
sum = 0
for i in range(len(l)):
    if l[i]%2==0:
        sum=sum+i
        print(i,l[i])
print(sum)
'''

'''
n= int(input("Enter the number "))
fact = 1
for i in range(1,n+1):
    fact = fact*i                       #or we can write as fact*=i
print(f'Factorial of {n} is {fact}')
'''
'''
data ={}
n = int(input("Enter the no.of students: "))
max_marks =0
for i in range(n):
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))
    if marks> max_marks:
        max_marks = marks
    data[name] = marks
print(data)
print("Maximum marks",max_marks)
'''
'''product = {}
sub_prod = []
bill = 0
total_bill =0
n = int(input("Enter number of products: "))
for i in range(n):
    prod_name = input("Enter the product name: ")
    price = int(input("Enter the price: "))
    quantity = int(input("Enter the no.of items: "))
    sub_prod = [price, quantity]
    product[prod_name] = sub_prod
    bill = price*quantity

    total_bill += bill
print(product)
print("total bill ",total_bill)
'''

n = int(input("Enter the no of products: "))
total_bill =0
products ={}
for i in range(n):
    product = input(f'Product - {i}: ')
    price = float(input(f'Price - {i}: '))
    quantity = int(input(f'Quantity - {i}: '))
    final_price = price*quantity
    total_bill += final_price
    products[product] = f'{price}*{quantity} = {final_price}'
print(products)
print("Total Bill: ",total_bill)
