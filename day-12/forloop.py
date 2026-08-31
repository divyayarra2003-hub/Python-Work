# sequential data types str list tuple set dict range
'''
syntax:
-------
for var in sequence:
    print(var)
'''

'''
s ='codegnan'
for ch in s:
    if ch in 'aeiouAEIOU':
        print(ch)
        '''

'''
l = [10,23,56,77,98,78,90,45,67,89]
for i in l:
    if i%2==0:
        print(i,"Even")
    else:
        print(i,"Odd")
        '''
'''
marks =(78,89,90,67,56,45,34,23,12)
for m in marks:
    if m>=35:
        print("pass",m)
    else:
        print("fail",m)
'''
'''
followers = {'divya','sri','eryx','nani','honey'}
for i in followers:
    print(i)
    '''

'''
bus = {'s1':'Booked','s2':'Booked','s3':'Available','s4':'Available','s5':'Booked'}
for seat in bus:
    if bus.get(seat) == 'Available':
        print(seat, bus.get(seat))
        '''
'''
for i in range(1,11):
    print(i)


for i in range(2,99,2):
    print(i)

for i in range(1,100,2):
print(i)
'''

n = int(input("Enter a number: "))
for i in range(1,11):
    print(f'{n}*{i}={n*i}')
