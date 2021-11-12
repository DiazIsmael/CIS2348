#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #3 Zylabs 10.17

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.00, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print("{} {} @ ${:.0f} = ${:.0f}".format(self.item_name, self.item_quantity, self.item_price, (self.item_price*self.item_quantity)))


if __name__ == "__main__":
    print("Item 1")
    name = input("Enter the item name:\n")
    price = float(input("Enter the item price:\n"))
    qty = int(input("Enter the item quantity:\n"))
    item1 = ItemToPurchase(name, price, qty)
    print()

    print("Item 2")
    name = input("Enter the item name:\n")
    price = float(input("Enter the item price:\n"))
    qty = int(input("Enter the item quantity:\n"))
    item2 = ItemToPurchase(name, price, qty)
    print()

    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print()
    print("Total: ${:.0f}".format((item1.item_price*item1.item_quantity) + (item2.item_price*item2.item_quantity)))
