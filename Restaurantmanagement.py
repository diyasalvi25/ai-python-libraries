class RestaurantManagementSystem:
    def __init__(self):
        self.menu = {
            1: {'name': 'Pizza', 'price': 250},
            2: {'name': 'Burger', 'price': 120},
            3: {'name': 'Pasta', 'price': 180},
            4: {'name': 'Coffee', 'price': 80}
        }
        self.order = []

    def show_menu(self):
        print("\n------ MENU ------")
        for item_id, item_info in self.menu.items():
            print(f"{item_id}. {item_info['name']} - Rs. {item_info['price']}")
        print("------------------\n")

    def take_order(self):
        while True:
            self.show_menu()
            try:
                choice = int(input("Enter item number to order (0 to finish): "))
                if choice == 0:
                    break
                if choice in self.menu:
                    quantity = int(input(f"Enter quantity for {self.menu[choice]['name']}: "))
                    self.order.append({'item': self.menu[choice]['name'], 
                                       'price': self.menu[choice]['price'],
                                       'quantity': quantity})
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def generate_bill(self):
        print("\n------ BILL ------")
        total = 0
        for item in self.order:
            item_total = item['price'] * item['quantity']
            print(f"{item['item']} x {item['quantity']} = Rs. {item_total}")
            total += item_total
        print("------------------")
        print(f"Total Amount: Rs. {total}")
        print("------------------\n")
        self.order.clear()

    def run(self):
        while True:
            print("1. Show Menu")
            print("2. Take New Order")
            print("3. Generate Bill")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.show_menu()
            elif choice == '2':
                self.take_order()
            elif choice == '3':
                self.generate_bill()
            elif choice == '4':
                print("Thank you for using the Restaurant Management System!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    rms = RestaurantManagementSystem()
    rms.run()