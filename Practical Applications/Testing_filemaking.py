inventory = [
    {
        "name": "copper coin",
        "quantity": 3,
        "points": 5
    },
    {
        "name": "silver coin",
        "quantity": 20,
        "points": 10,
    },
]

with open ("inventory.txt","w") as file:
    file.write("RPG Inventory\n")
    file.write (str(inventory))

item_list = []
for item in inventory:
    total_points = item["quantity"] * item["points"]
    item_list.append(total_points)
    print(item["name"],total_points)

grand_total = sum(item_list)
print(grand_total)

    

