#providing security to the data through public, private(__) and protected(_) attributes
#wrapping the data and methods into a single unit
'''
class Instagram:
    def __init__(self, username,password):
        self.username = username
        self.__password = password
        self._posts =[]

    def getpassword(self):
        return self.__password
    @property
    def accesspost(self):
        return self._posts
    def display(self):
        print(self.username, self.__password, self._posts)

divya = Instagram('divya','divya@123')
divya.display()
print(divya.username)
print(divya.getpassword())
print(divya.accesspost)
'''
#updating and accessing
class Instagram:
    def __init__(self, username,password):
        self.username = username
        self.__password = password
        self._posts =[]

    def getpassword(self):
        return self.__password
    
    def setpassword(self, newpassword):
        self.__password = newpassword

    @property
    def accesspost(self):
        return self._posts
    
    @accesspost.setter
    def accesspost(self, newpost):
        self._posts.append(newpost)

    def display(self):
        print(self.username, self.__password, self._posts)

divya = Instagram('divya','divya@123')
divya.display()
print(divya.username)
print(divya.getpassword())
print(divya.accesspost)

divya.username = 'sri'
divya.setpassword('sri@0907')
divya.accesspost = 'moon.png'
divya.accesspost = 'eryx.png'
divya.accesspost = 'arcane.png'

print(divya.username)
print(divya.getpassword())
print(divya.accesspost)