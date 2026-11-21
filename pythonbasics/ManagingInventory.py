inventory=["Apples","Bananas","Oranges","Grapes"]
inventory.append("Strawberries")
inventory.remove("Bananas")
item="Oranges"
if item in inventory:
    print(f"{item} are in stock")
else:
    print(f"{item} are out of stock")
print("Current inventory:",inventory)