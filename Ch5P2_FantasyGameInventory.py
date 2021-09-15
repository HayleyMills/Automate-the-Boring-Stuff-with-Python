##Imagine that a vanquished dragon’s loot is represented as a list of strings like this:
##dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
##Write a function named addToInventory(inventory, addedItems), where the
##inventory parameter is a dictionary representing the player’s inventory
##(like in the previous project) and the addedItems parameter is a list like
##dragonLoot. The addToInventory() function should return a dictionary that
##represents the updated inventory.
##Note that the addedItems list can contain multiples of the same item.


def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] = inventory.get(i)+1

def displayInventory(inventory):
    import pprint
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(v, k)
    print("Total number of items: " + str(item_total))
   
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)


displayInventory(inv)


