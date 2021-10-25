from tester1 import A

class B(A):
    def div(self,a,b):
        c=a/b
        print("Division of two numbers: + sttr(c)")
    def sum(self,a,b):
        c=a*a+b*b
        print(c)

objb=B()
objb.sum(10,15)
objb.mul(10,15)
objb.div(150,10)