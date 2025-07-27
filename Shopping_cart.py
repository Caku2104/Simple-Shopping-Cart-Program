
def add_items(*args):
    global cart
    global total
    
    for i in range(len(args)):
        cart.append(args[i])
        total += catalog.get(args[i])

def remove_item():
    done = False
    while not done:
        choice = input("Please choose an item to remove: ").lower()
        if not choice in catalog.keys():
            print("There is no such item. Please try again.")
        else:
            cart.remove(choice)
            total -= catalog[choice]
            print(f"{choice} has been removed.")
            next = input("Would you like to remove one more item? (to remove type 'yes', to not remove type anything else): ").lower()
            if len(cart) == 0:
                print("There is nothing you can remove.")
                done = True
            elif next == "yes":
                continue
            else:
                done = True

def view_cart():
    print(f"Your shopping cart has: {cart}")
    print(f"Running total: ${total:.2f}")

def checkout():
    print(f"Your total is: ${total:.2f}")
    print("Bye.")

import time


cart = []
total = 0.0

catalog = {"avocado": 3.49, "apple": 2.99, "banana": 1.99, "egg": 0.49, "bread": 0.49, "bacon": 4.99, "turkey": 10.99, "tuna": 4.59, "soda": 2.59, "water": 1.99, "chocolate": 3.49}

print("Welcome to the Shopping Cart Simulator.")
print(f"You can get the following products for the indicated price --> {catalog}")
print(".")
time.sleep(1)

print("Please pick the items you want. You can remove and add items after selecting as well.")
print("You can also pick everything in one go as well.")
print("You can use 'remove' command to remove an item from your cart.")
print("You can use 'view' command to learn what you have in your cart.")
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("After picking once, you can quit the program whenever you want by writing 'quit' separately from the other products.")
print(".")
time.sleep(1)

get_items = ""
while get_items != "quit":
    get_items = input("Please select:")
    if get_items == "quit":
        continue
    elif get_items == "remove" and len(cart) >= 1:
        remove_item()
    elif get_items == "view" or get_items == "remove":
        if len(cart) == 0:
            print("You have nothing in your cart.")
        else:
            view_cart()
    elif not get_items in catalog.keys() and not get_items == "remove" and not get_items == "view":
        print("You have entered an invalid input. Please try again.")
    else:
        item_list = get_items.split()
        add_items(*item_list)

print(f"Your shopping cart has: {cart}")
checkout()