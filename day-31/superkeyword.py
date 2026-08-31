'''
class whatsappv1:
    def messaging(self):
        print("You can message")
class whatsappv2(whatsappv1):
    def messaging(self):
        super().messaging()
        print("You can add stickers and emojis")
class whatsappv3(whatsappv2):
    def messaging(self):
        super().messaging()
        print("You can send files and audio texts")
c=whatsappv3()
c.messaging()
'''
class whatsappv1:
    def messaging(self):
        print("You can message")
class whatsappv2:
    def messaging(self):
        print("You can add stickers and emojis")
class whatsappv3(whatsappv1, whatsappv2):
    def messaging(self):
        whatsappv1.messaging(self)
        whatsappv2.messaging(self)
        print("You can send files and audio texts")
c=whatsappv3()
c.messaging()