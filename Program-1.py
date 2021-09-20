
class calure:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self,ch,c=0):
        
       
        if ch==1:
            c=self.a+self.b
            print('Addtion  :',c)
            print()
        elif ch==2:
            c=self.a-self.b
            print('Subtraction  :',c)
            print()
        elif ch==3:
            c=self.a*self.b
            print('Multiplication  :',c)
            print()
        elif ch == 4:
            if self.b == 0:
                print('Enter value great the 0')
                print()
            else:
                c=self.a/self.b
                print('Division   :',c)
                print()
        else:
            print('Plz Enter Number Only')
            print()
while(True):
    print('Chosic Any One Option :\n 1:Addtion \n 2:Subtraction \n 3:Multiplication \n 4:Division')
    ch=int(input('Enter Your Choisc     :'))
    a=float(input("Enter The Number's    :"))
    b=float(input("Enter The Number's    :"))
    print('--'*30)
        
    obj =calure(a,b)
    obj.show(ch)
            
            
