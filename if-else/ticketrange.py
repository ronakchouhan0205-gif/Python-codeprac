age=int(input("Enter your age: "))
days=input("Enter the day of the week: ")
weekend=["saturday","sunday"]
if(days in weekend):
    print("Your ticket price is $300")
elif(age>=1 and age<=11):
    print("Your ticket price is $110")
elif(age>=12 and age<=59):
    print("Your ticket price is $250")
elif(age>=60):
    print("Your ticket price is $150")
elif(age<=0):
    print("Invalid age entered")
