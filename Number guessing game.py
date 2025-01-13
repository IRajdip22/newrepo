import random

number = random.randint(1,5)
print("Number",number)

trials = 5
message = "You Lost!!!"

while trials>0:
    print(f'{trials} attempt left')
    trials -= 1
    user_input = int(input("Enter a number: "))

    if user_input ==number:
        message = "You won!!!"
        break
    else:
        print("Try again")
        continue    

print(message)
