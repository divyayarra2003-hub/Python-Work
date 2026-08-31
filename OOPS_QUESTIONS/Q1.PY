class user:
    def __init__(self,name,email,phone,password):
        self.name=name
        self.email=email
        self.phone=phone
        self.password=password
    def registration(self):
        if self.name!=True:
            print("Name is required")
        elif self.email!=True:
            print("Email is required")
        elif self.phone!=True:
            print("Phone number is required")
        elif self.password!=True:
            print("password is required")