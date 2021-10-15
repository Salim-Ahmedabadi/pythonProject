class A:
    def welcome(self):
        print("Welcome to Texas!")

        def sum(a,b):
            c=a+b
            print("Sum of two numbers: " + str(c))
obj=A() #object of a class
obj.welcome()
obj.sum(10,10)
