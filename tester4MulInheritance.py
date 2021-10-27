from tester1 import A
from tester5 import B

class C(A,B):
    def div(self,a,b):
        c=a/b
        print(c)

objc=C()
objc.sum(10,20)
objc.mul(10,20)
objc.div(20,10)
objc.sqrmul(10)
