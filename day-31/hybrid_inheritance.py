class whatsappv1:
    def messaging(self):
        print("You can message")
class whatsappv2:
    def calls(self):
        print("You can make audio and video calls")
class whatsappv3(whatsappv1, whatsappv2):
    def status(self):
        print("You can add status for 24 hours")
class whatsappv4(whatsappv3):
    def extramessage(self):
        print("You can add emojis, stickers and gifts")
a=whatsappv1()
a.messaging()
b=whatsappv2()
b.calls()
c=whatsappv3()
c.messaging()
c.calls()
c.status()
d=whatsappv4()
d.messaging()
d.calls()
d.status()
d.extramessage()