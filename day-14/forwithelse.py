# whenever break executes, else will not execute, if break doesn't execute, else will execute
'''
for i in range(1,10):
    if i==5:
        break
    print(i)
else:
    print("End of the loop")
'''
'''
for i in range(1,10):
    if i==15:
        break
    print(i)
else:
    print("End of the loop")
'''
'''
#phone pin checking
pin = 1234
for _ in range(5):
    epin = int(input("Enter the pin: "))
    if epin==pin:
        print("Unlock phone")
        break
    else:
        print("Invalid pin")
else:
    print("Try again after 30 seconds")
    '''
'''
#factors of a number
n = int(input("Enter the number: "))
print("Factors: ", end=' ')
for i in range(1, n+1):
    if n%i==0:
        print(i,end=' ')
        '''
'''
#prime number
n = int(input("Enter the number: "))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("Prime number")
else:
    print("Not a prime number")
    '''
#prime number
n = int(input("Enter the number: "))
for i in range(2,n//2+1):
    if n%i==0:
        print("Not a prime number")
        break
else:
    print("Prime number")