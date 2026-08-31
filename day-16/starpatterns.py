'''n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print()
'''

'''n = int(input('Enter the size: '))
for i in range(n):
    for space in range(n-i-1):
        print(" ",end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
    '''

'''n=int(input("ENter the size: "))
for i in range(n):
    for space in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()
    '''

'''n=int(input("Enter the size"))
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    '''

'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1 or i==n//2 or j==n//2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
    '''

'''
n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if(i%2==0 or j%2==0):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
    '''

'''
n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if(i==j or i+j==n-1):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    '''

'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or j==n-1 or i==n//2):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    '''

'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or j==n-1 or i==n-1 or i==n//2):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    '''

'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if(j==0 or i%2==0):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
#F
n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n//2):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
#G
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or (i==n-1 and j<=m) or (j==m and i>=m) or (i==m and j>=m) or (j==n-1 and i>=m)):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
#H
n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1 or i==n//2):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
#I
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==n//2):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
#J
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if(i==0 or j==n//2 or (i==n-1 and j<=m)):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
#k
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or (i==m and j<=m) or (i+j==n-1 and i<=m) or (i==j and i>=m):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
#L
n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if(j==0 or i==n-1):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    '''

#M
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1 or (i==j and i<=m) or (i+j==n-1 and i<=m)):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    
    
'''
#N
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1 or i==j):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
#O
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if(j==0 or i==0 or i==n-1 or j==n-1):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
#p
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==m or (j==n-1 and i<=m)):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
