import tkinter as tk
from tkinter import messagebox

class VendingMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Vending Machine")
        self.root.geometry("400x300")

        # Items in the vending machine with their prices
        self.items = {
            "Soda": 1.50,
            "Chips": 1.00,
            "Candy": 0.75,
            "Water": 1.00,
            "Chocolate": 1.25
        }

        # Variable to store the selected item
        self.selected_item = tk.StringVar()
        self.selected_item.set("Select an item")

        # Variable to store the amount of money inserted
        self.money_inserted = tk.DoubleVar()
        self.money_inserted.set(0.0)

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Label for item selection
        tk.Label(self.root, text="Select Item:").grid(row=0, column=0, padx=10, pady=10)

        # Dropdown menu for item selection
        item_menu = tk.OptionMenu(self.root, self.selected_item, *self.items.keys())
        item_menu.grid(row=0, column=1, padx=10, pady=10)

        # Label for money insertion
        tk.Label(self.root, text="Insert Money:").grid(row=1, column=0, padx=10, pady=10)

        # Entry for money insertion
        tk.Entry(self.root, textvariable=self.money_inserted).grid(row=1, column=1, padx=10, pady=10)

        # Button to purchase item
        tk.Button(self.root, text="Purchase", command=self.purchase_item).grid(row=2, column=0, columnspan=2, pady=10)

        # Label to display change
        self.change_label = tk.Label(self.root, text="Change: $0.00")
        self.change_label.grid(row=3, column=0, columnspan=2, pady=10)

    def purchase_item(self):
        item = self.selected_item.get()
        money = self.money_inserted.get()

        if item == "Select an item":
            messagebox.showerror("Error", "Please select an item.")
            return

        if item not in self.items:
            messagebox.showerror("Error", "Invalid item selected.")
            return

        price = self.items[item]

        if money < price:
            messagebox.showerror("Error", "Insufficient funds.")
            return

        change = money - price
        self.change_label.config(text=f"Change: ${change:.2f}")
        messagebox.showinfo("Success", f"Enjoy your {item}!")

        # Reset the money inserted
        self.money_inserted.set(0.0)

if __name__ == "__main__":
    root = tk.Tk()
    vending_machine = VendingMachine(root)
    root.mainloop()