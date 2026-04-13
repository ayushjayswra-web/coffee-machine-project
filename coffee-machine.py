class CoffeeMachine:
    def __init__(self):
        self.water = 1000
        self.milk = 500
        self.coffee = 150
        self.money = 0

    def show_resource(self):
        print("\n--- Coffee Machine Resources ---")
        print(f"Water : {self.water} ml")
        print(f"Milk  : {self.milk} ml")
        print(f"Coffee: {self.coffee} g")
        print(f"Money : ₹{self.money}")

    def check_resources(self, water, milk, coffee):
        if self.water < water:
            print("Not enough water!")
            return False
        if self.milk < milk:
            print("Not enough milk!")
            return False
        if self.coffee < coffee:
            print("Not enough coffee!")
            return False
        return True

    def make_coffee(self, coffee_type, water, milk, coffee, price):
        if self.check_resources(water, milk, coffee):
            print("\nMaking your coffee...")
            print("Heating water...")
            print("Grinding coffee beans...")
            print("Mixing ingredients...")
            print(f"Your {coffee_type} is ready!\n")

            self.water -= water
            self.milk -= milk
            self.coffee -= coffee
            self.money += price

    def menu(self):
        while True:
            print("\n===== Coffee Menu =====")
            print("1. Espresso (₹50)")
            print("2. Latte (₹70)")
            print("3. Cappuccino (₹80)")
            print("4. Show Resources")
            print("5. Exit")

            try:
                choice = int(input("Select option: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            if choice == 1:
                self.make_coffee("Espresso", 50, 0, 18, 50)
            elif choice == 2:
                self.make_coffee("Latte", 200, 150, 24, 70)
            elif choice == 3:
                self.make_coffee("Cappuccino", 250, 100, 24, 80)
            elif choice == 4:
                self.show_resource()
            elif choice == 5:
                print("Thank you for using Coffee Machine!")
                break
            else:
                print("Invalid choice. Try again.")


# Run program
if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.menu()