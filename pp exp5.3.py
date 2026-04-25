inventory = {
    "apple": 10,
    "banana": 5
}

item = "apple"
new_stock = 20

if item in inventory:
    inventory[item] += new_stock
else:
    inventory[item] = new_stock

print(inventory)
