items=[]
 
while True:
    item = input ('Add items. Type done when you are done :')
    if item.lower() == "done":
        break
    items.append(item)

print("Items in cart:", items)
 