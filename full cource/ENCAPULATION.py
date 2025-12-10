class senthil:
    def __init__(self,fuck):
        self.__myname=fuck
        
class dub(senthil):
    super().__init__(fuck)
    
    def display(self):
        
        print(self.__myname)
        
a=dub("fuck")


a.display()


    
