#Timur ID:2025088

class Item:
    def __init__(self, name, price):
        self.name = name 
        self.price = price 


class ShoppingCart:
    def __init__(self):
        self.items = []

    def showItems(self):
        for i in self.items:
            print(i.name)    
    
    def addItem(self, item):
        self.items.append(item)
    
    def removeItem(self,item):
        self.items.remove(item)
      
    def calculateTotal(self):
        sum = 0
        for i in self.items:
            sum+=i.price
        print(sum)

item1 = Item("Cola", 3000) 
item2 = Item("Cheeps", 6000)    
      
cart1 = ShoppingCart()
cart1.addItem(item1)
cart1.addItem(item2)
cart1.removeItem(item1)
cart1.showItems()
cart1.calculateTotal()

