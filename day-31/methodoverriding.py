class Hotstar:
    def __init__(self,name):
        print(f'Welcome to the hotstar, {name}')
    def login(self):
        print("You can login to the hotstar")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("you can search")
    def playcontrollers(self):
        print("pause.resume.play")
    def history(self):
        print("you can seee the recent video")
    def ads(self):
        print("Ads will run")
    def quality(self):
        print("quality is low")
    def access(self):
        print("you have only access for limited things")
    def download(self):
        print("You cannot download")
class Premium:
    def ads(self):
        print("Ads will not run")
    def quality(self):
        print("quality is high")
    def access(self):
        print("you have unlimited access")
    def download(self):
        print("You can download with high quality")
a = Hotstar('sri')
a.download()
b=Premium()
b.download()