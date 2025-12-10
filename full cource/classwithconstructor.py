class phone():
    pt="c trype"
    def __init__(self,name,cost):
        self.ne=name
        self.ct=cost
    def dplay(self):
          
          print("brankd name",self.ne)
          print("cost of it ",self.ct)
          print("type of charing",phone.pt)
    @classmethod
    def fuck(cls):
        cls.pt="fuck you acc"
        print("changed into p",cls.pt)
a=phone("senthil","12124")



phone.fuck()

