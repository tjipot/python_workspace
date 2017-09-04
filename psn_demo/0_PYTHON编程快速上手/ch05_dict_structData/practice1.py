# p93'inventory.py': item list for the game, @20170110;

stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def inventoryDisplay(invDict):
    print('Inventory:')
    itemTotal = 0
    for key, value in invDict.items():
        print(str(value) + ' ' + key)
        itemTotal += value
    print('Total number of items: ' + str(itemTotal))

inventoryDisplay(stuff)
