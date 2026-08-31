class whatsappv1:
    def messaging(self):
        print("You can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("You can make audio and video calls")
a=whatsappv1()
a.messaging()
b=whatsappv2()
b.messaging()
b.calls()