try:
    obj=open("D:\\Selenium_Python\\TestData\\TestData5.txt",'r')
    #print(obj.read())
    print(obj.readline())
    print(obj.tell())
    print(obj.tell(5))
    print(obj.tell())
except:
    print("There is a file not found error")
finally: # optional
    print("This is my other line of code")



