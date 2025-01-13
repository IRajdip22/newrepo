def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("SELECT OPRATION")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice: ")
    if choice in ("1","2","3","4"):
        try:
            num1 = float(input("Enter Number 1: "))
            num2 = float(input("Enter Number 2: "))
        except Valuerror:
            print("Invalid Input: \n Please enter anumber between 1 to 4")
            continue
        if choice == "1":
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == "2":
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice =="3":
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice =="4":
            print(num1,"/",num2,"=",subtrace(num1,num2))
        New_calculation = input("Do you want do any other calculation? (yes/no): ")
        if New_calculation == "no":
            break
    else:
        print("Invalid input")



