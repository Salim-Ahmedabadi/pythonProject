age=input("Enter your age: ")
#When user inputs age at the runtime, it will take default value as string
print(age)

if(int(age)>=60):
    print("Old age")
elif(int(age)>18):
    print("Adult")
else:
    print("Child")