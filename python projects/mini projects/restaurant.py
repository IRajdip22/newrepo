menu = {

    "coffee": 3.45,
    "tea": 2.50,
    "sandwich": 5.50,
    "soup": 3.25,
    "water": 1.25,
    "pizza": 7.00,
    "salad": 4.25,
    "pasta": 5.50,
}

print("Welcome to the restaurant!")
print("Pizza: £7.00\nSalad: £4.25\nPasta: £5.50\nCoffee: £3.45\nTea: £2.50\nSandwich: £5.50\nSoup: £3.25\nWater: £1.25")

Total_Bill = 0
item1 = input(str("pleace select an item: "))

if item1 in menu:
    Total_Bill += menu[item1]
    print(f"Total Bill: £{Total_Bill}")
else:
    print("Item not available")

anything_else = input("Would you like anything else? (yes/no): ")

if anything_else == "yes":
    item2 = input(str("pleace select an item: "))
    if item2 in menu:
        Total_Bill += menu[item2]
        print(f"Total Bill: £{Total_Bill}")
    else:
        print("Item not available")
else:
    print(f"Your total bill is £{Total_Bill}")        