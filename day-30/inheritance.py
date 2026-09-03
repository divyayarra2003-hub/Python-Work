'''
1.single: acquiring properties from parent to child class                            A->B
2.multiple : many parents, single child                                              A,B,C->D  
3.multi level: inheriting from parent to child classes multiple times                A->B->C
4.Hierarchical: single parent, multiple child                                        A-> B,C,D
5.Hybrid: combination of the above inheritances
'''
class whatsappV1:
    def __init__(self, name):
        self.name = name
        print(f'Welcome to whatsapp version1 {self.name}')
    def messaging(self):
        print("You can send the messages")
class whatsappV2(whatsappV1):
    def __init__(self,name):
        self.name=name
        print(f'Welcome to whatsapp version2 {self.name}')
    def calls(self):
        print("You can make audio and video calls")

divya = whatsappV1('divya')
divya.messaging()

sri = whatsappV2('Sri')
sri.messaging()
sri.calls()