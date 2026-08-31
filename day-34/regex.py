import re
'''
#pattern = r'code'
pattern = r'[0-9]'
#pattern = r'[a-zA-Z]'
text = 'codegnan 2026 python version 3.14'
#res = re.match(pattern,text)
#res = re.search(pattern,text)
res = re.findall(pattern,text)
print(res)
#print(res.group() if res else "Pattern not found")
'''
'''
pattern = r'[0-9]'
text = 'codegnan 2026 python version 3.14'
res = re.finditer(pattern, text)
for i in res:
    print(i.group(),i.start())
    '''
'''
pattern = r'[0-9]{10}'
text = '9876543210'

res = re.fullmatch(pattern,text)
print(res.group() if res else "Pattern not found")
'''
'''
pattern = r'[,(#)]'
text = 'java,python(html#css'
res = re.split(pattern,text)
print(res)
'''
'''
pattern = r'[a-z]'
text = 'python version 3.14, batch-63'
res = re.sub(pattern, '*', text)
print(res)
'''
'''
pattern = r'e.t'
text = 'e@t eaat eat eet ett ect Egjfdt hfffffffffmdfkmnd'
res = re.findall(pattern,text)
print(res)
'''
'''
pattern = r'^(91)'
text = '91 9876543210'
res = re.findall(pattern,text)
print(res)
'''
'''
pattern = r'0$'
text = '91 9876543210'
res = re.findall(pattern,text)
print(res)
'''
'''
#pattern = r'to*'
pattern = r'to+'
text = 'today is not tomorrow tomorrow is not a holiday toooooo'
res = re.findall(pattern,text)
print(res)
'''
'''
pattern1 = r'ab*'
pattern2 = r'ab+'
text = 'a ab abbb abbbbbb abb'
res1 = re.findall(pattern1,text)
res2 = re.findall(pattern2,text)
print(res1)
print(res2)
'''
'''
pattern = r'[91 | 0]'
text = '09332'
res = re.findall(pattern,text)
print(res)
'''
pattern = r'[aeiouAEIOU]'
text = 'Python programming'
res = re.findall(pattern,text)
print(res)

