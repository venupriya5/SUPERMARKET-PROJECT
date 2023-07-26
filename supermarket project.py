print(10*'---')
print(20*"  ","D-MART",20*"  ")
import datetime

class Supermarket:
    def __init__(self):
        self.inventory = {
            'apple': 5.0,
            'banana': 1.0,
            'grapes':5.0,
            'milk': 3.0,
            'bread': 2.0,
            'eggs': 2.5,
            'rice':40.0,
            'salt':10.0,
            'turmeric powder':5.0,
            'magi':50.0,
            'chocolate':10.0,
            'biscuites':20.0,
            'icecream':15.0,
            

        }
        self.cart = {}
        self.total_price = 0.0

    def add_to_cart(self, item, quantity):
        if item in self.inventory:
            if item in self.cart:
                self.cart[item] += quantity
            else:
                self.cart[item] = quantity
            print(f"{quantity} {item}(s) added to the cart.")
        else:
            print(f"{item} is not available in the supermarket.")

    def calculate_total(self):
        self.total_price = sum(self.inventory[item] * quantity for item, quantity in self.cart.items())
        return self.total_price

    def generate_bill(self):
        
        print(10*"  --","D-MART",10*"--  ")
        print("\n*********************** BILL ************************")

        current_datetime = datetime.datetime.now()
        # Get the current date
        current_date = current_datetime.date()

        # Get the current time
        current_time = current_datetime.time()

        # Print the current date and time

        print("  "*5,"Current Date:", current_date)
        print("  "*5,"Current Time:", current_time)
        print( )

        for item, quantity in self.cart.items():
            price = self.inventory[item] * quantity
            print(f"{item} x {quantity} = ₹{price:.2f}")
        print("*****************************************************")
        print(15*"  ",f"Total: ₹{self.total_price:.2f}")
        print("___"*10)

def main():
    supermarket = Supermarket()

    print(5*"__","Welcome to the D-MART!",5*"__")
    print("Available items:")
    for item in supermarket.inventory.keys():
        print(f" - {item}")

    
    while True:
        item = input("Enter the item you want to buy (or 'done' to finish): ").lower()
        if item == 'done':
            break
        quantity = int(input("Enter the quantity: "))
        supermarket.add_to_cart(item, quantity)

    total_price = supermarket.calculate_total()
    supermarket.generate_bill()

if __name__ == "__main__":
    main()
