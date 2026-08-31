'''
#11th: reverse a string
s = input()
s1 = s[::-1]
print(s1)

#12th palindrome
s = input("Enter string : ")
s1 = s[::-1]
if s==s1:
    print(f'{s} is a palindrome')
else:
    print(f'{s} is not a palindrome')

#13th vowel and consonant count
s = input("Enter the string: ").strip()
vowels=['a','e','i','o','u']
vowel = []
consonant = []
for char in s.lower():
    if char in vowels:
        vowel.append(char)
    elif char.isalpha():
        consonant.append(char)
print("vowel count: ",len(vowel))
print("Consonant count: ",len(consonant))

#16th remove duplicate characters from string
s = input().strip()
s1 = set(s)
print(s1)
'''
#19th count words in a sentence
s = input("Enter a sentence: ").strip(' ')
print(len(s))

