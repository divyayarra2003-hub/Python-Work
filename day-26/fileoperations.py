'''
file = open('pfs-63','r')
print(file.read())
file.seek(0)                        
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()
'''
'''
seek(0) defines the index, and it starts from 0 index because the cursor moves down 
and can't read from the starting and the remaining things will not be executed
'''
'''
with open('pfs-63.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    '''
'''
with open('mysql.txt','w') as file:
    file.write('Mysql is used as a database to store data in the form of tables')
    '''
'''
with open('pfs-63.txt','w') as file:
    file.write('We are learning python full stack at codegnan')
    #it overrides the previous content in the pfs-63.txt
    '''

'''with open('pfs-63.txt','a') as file:
    file.write(' .And the technologies they are providing are python, flask, mysql, html, css, bootstrap, javascript, reactjs,dsa and gen ai')
    '''
'''
with open('mysql.txt','a+') as file:
    file.write('. It can be used with python for the backend')
    file.seek(0)
    print(file.read())
    '''
'''
with open('mysql.txt','r+') as file:
    print(file.read())
    file.write('. If we learn postgresql, then it will be more useful')
    '''
with open('mysql.txt', 'w+') as file:
    file.write('Learning mysql itself is not that useful')
    file.seek(0)
    print(file.read())