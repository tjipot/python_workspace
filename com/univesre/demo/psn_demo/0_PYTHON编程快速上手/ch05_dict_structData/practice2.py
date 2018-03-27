# p94'addToInventory.py': could add items into the dict, @20170110;

stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def inventoryDisplay(invDict):
    print('Inventory:')
    itemTotal = 0
    for key, value in invDict.items():
        print(str(value) + ' ' + key)
        itemTotal += value
    print('Total number of items: ' + str(itemTotal))

inventoryDisplay(stuff)

# New code below;
def addToInventory(inventory, addedItems):
    for item in addedItems:
        #count = inventory.get(item, 0)
        if item not in inventory:
            inventory[item] = 0
        inventory[item] += 1
    return inventory    # Should return the reference of inventory, otherwise, return None by default: "AttributeError: 'NoneType' object has no attribute 'items'";

inv = {'gold coin':42, 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
inventoryDisplay(inv)
# New code ends;




