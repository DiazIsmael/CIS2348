#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #3 Zylabs 10.17

class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0.00, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print("{} {} @ ${:.0f} = ${:.0f}".format(self.item_name, self.item_quantity, self.item_price, (self.item_price*self.item_quantity)))

    def print_item_description(self):
        print("{}: {}".format(self.item_name, self.item_description))


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, itemtopurchase):
        self.cart_items.append(itemtopurchase)

    def remove_item(self, itemtoremove):
        itemslist = []
        for item in self.cart_items:
            itemslist.append(item.item_name)

        i = 0
        if itemtoremove in itemslist:
            for i in range(len(itemslist)):
                if self.cart_items[i].item_name == itemtoremove:
                    del self.cart_items[i]
        else:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, itemtopurchase):
        itemslist = []
        for item in self.cart_items:
            itemslist.append(item.item_name)

        if itemtopurchase.item_name in itemslist:
            for i in range(len(self.cart_items)):
                if self.cart_items[i].item_name == itemtopurchase.item_name:
                    self.cart_items[i].item_quantity = itemtopurchase.item_quantity
        else:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        numitems = 0
        for item in self.cart_items:
            numitems += item.item_quantity
        return numitems

    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.item_price * item.item_quantity

        return total

    def print_total(self):
        if not self.cart_items:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items: {}".format(self.get_num_items_in_cart()))
            print()
            print("SHOPPING CART IS EMPTY")
            print()
            print("Total: ${:.0f}".format(self.get_cost_of_cart()))
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items: {}".format(self.get_num_items_in_cart()))
            print()
            for item in self.cart_items:
                total = item.item_price * item.item_quantity
                print("{} {:.0f} @ ${:.0f} = ${:.0f}".format(item.item_name, item.item_quantity, item.item_price, total))
            print()
            print("Total: ${:.0f}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    option = ""
    while option != "q":
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print()
        option = input("Choose an option:\n")
        while option != "a" and option != "r" and option != "r" and option != "c" and option != "i" and option != "o" and option != "q":
            option = input("Choose an option:\n")

        if option == "a":
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            desc = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            qty = int(input("Enter the item quantity:\n"))
            newitem = ItemToPurchase(name, desc, price, qty)
            cart.add_item(newitem)

        elif option == "r":
            print("\nREMOVE ITEM FROM CART")
            itemremove = input("Enter name of item to remove:\n")
            cart.remove_item(itemremove)

        elif option == "c":
            print("\nCHANGE ITEM QUANTITY")
            item = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            changeditem = ItemToPurchase(item, "", 0, quantity)
            cart.modify_item(changeditem)

        elif option == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif option == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        elif option == "q":
            break
        else:
            pass


if __name__ == "__main__":
    customername = input("Enter customer's name:\n")
    todaysdate = input("Enter today's date:\n")
    shoppingcart = ShoppingCart(customername, todaysdate)

    print()
    print("Customer name: {}".format(shoppingcart.customer_name))
    print("Today's date: {}".format(shoppingcart.current_date))
    print_menu(shoppingcart)

"""    
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
"""
