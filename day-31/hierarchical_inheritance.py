class whatsappv1:
    def messaging(self):
        print("You can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("You can make audio and video calls")
class whatsappv3(whatsappv1):
    def status(self):
        print("You can add status for 24 hours")
a=whatsappv1()
a.messaging()
b=whatsappv2()
b.messaging()
b.calls()
c=whatsappv3()
c.messaging()
c.status()