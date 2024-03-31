class Scope():
    attr1=1; attr2=2
    def __init__(self):
        self.attr1 = -1; Scope.attr2 = 20
    def m(self):
        self.attr1 =-10; Scope.attr3 = 30
    def prt(self):
        attr1=attr2="local"
        print(self.attr1,self.attr2,end=" ")
        print(Scope.attr1,Scope.attr2,end=" ")
        try:
            print(Scope.attr3,end=" ")
        except:
            print("NO",end=" ")
        print(attr1,attr2)
