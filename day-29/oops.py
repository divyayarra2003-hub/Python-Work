class Flipkart:
    products = {'shirts':1000, 'handbag':2000, 'pants':3000}
    discount =30

    @classmethod
    def display(cls):
        print(cls.products)

    @staticmethod
    def displaydiscount():
        print(f"Discount is {Flipkart.discount}%")

    def userinfo(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"Hello {self.name}, Welcone to the flipcart")

'''dheeraj = Flipkart()
dheeraj.userinfo("Dheeraj", "1234567890", "123 Main Street")
dheeraj.displaydiscount()
dheeraj.display()
'''
divya = Flipkart()
divya.userinfo("Divya", "0987654321", "456 Elm Street")
divya.displaydiscount()
divya.display()
print(divya.products)
print(divya.name)


Flipkart.displaydiscount()
Flipkart.display()
print(Flipkart.products)
#using object --> instance, class, static methods, class variables, instance variables
#using class --> class method, static method, class variables
'''
sri = Flipkart()
sri.userinfo("Sri", "5678901234", "789 Oak Avenue")
sri.displaydiscount()
sri.display()
'''