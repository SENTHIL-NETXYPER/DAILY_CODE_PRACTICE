a=int(input("fifrst numebr: "))
b=int(input("2nd numebr: "))

for i in range(a,b+1  ):
      
      if a>1:
            for x in range(2,i):
                  if i%x==0:
                        break
            else:
                    print(i)
             
          
   
