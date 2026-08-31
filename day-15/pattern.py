'''
for i in range(5):
    for j in range(7):
        print("*", end=' ')
    '''
'''
for i in range(5):                      #to print stars in rows
    for j in range(7):                  #to print stars in columns
        print('*', end=' ')             #prints the j loop in next column
    print()                             #prints the i loop in next row
    '''
'''
for row in range(5):
    for col in range(5):
        print(row,end=' ')
    print()
    '''
'''
for row in range(5):
    for col in range(5):
        print(col,end=' ')
    print()
    '''
'''
for row in range(5):
    for col in range(5):
        print(row+col, end=' ')
    print()
    '''
'''
for row in range(5):
    for col in range(5):
        print(col%2, end=' ')
    print()
    '''
'''
for row in range(5):
    for col in range(5):
        print((row+col)%2, end=' ')
    print()
    '''
'''
for row in range(5):
    for col in range(row+1):
        print("*",end=' ')
    print()
    '''

for row in range(5):
    for col in range(5-row):
        print("*",end=' ')
    print()