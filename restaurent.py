import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🍽️ Bachelors Kitchen")
        self.root.geometry("700x600")
        self.root.configure(bg="#f8f4f4")

        self.items_list = []
        self.order_items = []

        self.setup_styles()
        self.main_menu()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')

        style.configure("TFrame", background="#f8f4f4")
        style.configure("TLabel", background="#f8f4f4", font=("Segoe UI", 12))
        style.configure("Header.TLabel", font=("Segoe UI", 20, "bold"), foreground="#3f3f3f")
        style.configure("TButton", font=("Segoe UI", 12), padding=10, background="#007acc", foreground="white")
        style.map("TButton", background=[("active", "#005b99")])

        style.configure("TEntry", font=("Segoe UI", 12))

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_screen()

        ttk.Label(self.root, text="🍽️ Welcome to Bachelors Kitchen!", style="Header.TLabel").pack(pady=30)

        ttk.Button(self.root, text="🛠️ Admin Login", command=self.admin_login).pack(pady=10)
        ttk.Button(self.root, text="👨‍🍽️ Customer Login", command=self.customer_login).pack(pady=10)
        ttk.Button(self.root, text="❌ Exit", command=self.root.quit).pack(pady=10)

    # ------------ Admin Functions ------------
    def admin_login(self):
        self.clear_screen()
        ttk.Label(self.root, text="🛠️ Admin Login", style="Header.TLabel").pack(pady=20)

        username = ttk.Entry(self.root)
        password = ttk.Entry(self.root, show="*")

        for label, entry in zip(["Username:", "Password:"], [username, password]):
            ttk.Label(self.root, text=label).pack()
            entry.pack(pady=5)

        def check_login():
            if username.get() == "admin" and password.get() == "admin":
                self.admin_dashboard()
            else:
                messagebox.showerror("Login Failed", "Invalid admin credentials.")

        ttk.Button(self.root, text="Login", command=check_login).pack(pady=10)
        ttk.Button(self.root, text="🔙 Back", command=self.main_menu).pack()

    def admin_dashboard(self):
        self.clear_screen()
        ttk.Label(self.root, text="🛠️ Admin Dashboard", style="Header.TLabel").pack(pady=20)

        ttk.Button(self.root, text="➕ Add Item", command=self.add_item).pack(pady=5)
        ttk.Button(self.root, text="🗑️ Delete Item", command=self.delete_item).pack(pady=5)
        ttk.Button(self.root, text="📋 View Items", command=self.view_items).pack(pady=5)
        ttk.Button(self.root, text="🔙 Back", command=self.main_menu).pack(pady=10)

    def add_item(self):
        self.clear_screen()
        ttk.Label(self.root, text="➕ Add Menu Item", style="Header.TLabel").pack(pady=20)

        recipe = ttk.Entry(self.root)
        price = ttk.Entry(self.root)

        ttk.Label(self.root, text="🍲 Recipe Name:").pack()
        recipe.pack(pady=5)
        ttk.Label(self.root, text="💰 Price ($):").pack()
        price.pack(pady=5)

        def add_to_menu():
            try:
                name = recipe.get()
                cost = float(price.get())
                self.items_list.append({"recipe": name, "price": cost})
                messagebox.showinfo("Success", f"'{name}' added to menu.")
                self.admin_dashboard()
            except ValueError:
                messagebox.showerror("Error", "Enter a valid price.")

        ttk.Button(self.root, text="Add", command=add_to_menu).pack(pady=10)
        ttk.Button(self.root, text="🔙 Back", command=self.admin_dashboard).pack()

    def delete_item(self):
        self.clear_screen()
        ttk.Label(self.root, text="🗑️ Delete Menu Item", style="Header.TLabel").pack(pady=20)

        entry = ttk.Entry(self.root)
        ttk.Label(self.root, text="Enter Recipe Name:").pack()
        entry.pack(pady=5)

        def remove_item():
            name = entry.get()
            for item in self.items_list:
                if item['recipe'].lower() == name.lower():
                    self.items_list.remove(item)
                    messagebox.showinfo("Deleted", f"'{name}' removed.")
                    self.admin_dashboard()
                    return
            messagebox.showerror("Not Found", f"No item called '{name}'.")

        ttk.Button(self.root, text="Delete", command=remove_item).pack(pady=10)
        ttk.Button(self.root, text="🔙 Back", command=self.admin_dashboard).pack()

    def view_items(self):
        self.clear_screen()
        ttk.Label(self.root, text="📋 Menu Items", style="Header.TLabel").pack(pady=20)

        if not self.items_list:
            ttk.Label(self.root, text="No items in the menu yet.").pack(pady=10)
        else:
            for item in self.items_list:
                ttk.Label(self.root, text=f"🍛 {item['recipe']} — ${item['price']:.2f}").pack()

        ttk.Button(self.root, text="🔙 Back", command=self.admin_dashboard).pack(pady=10)

    # ------------ Customer Functions ------------
    def customer_login(self):
        self.clear_screen()
        ttk.Label(self.root, text="👨‍🍽️ Customer Login", style="Header.TLabel").pack(pady=20)

        username = ttk.Entry(self.root)
        password = ttk.Entry(self.root, show="*")

        for label, entry in zip(["Username:", "Password:"], [username, password]):
            ttk.Label(self.root, text=label).pack()
            entry.pack(pady=5)

        def login_customer():
            if username.get() == "customer" and password.get() == "customer":
                self.customer_dashboard()
            else:
                messagebox.showerror("Login Failed", "Invalid customer credentials.")

        ttk.Button(self.root, text="Login", command=login_customer).pack(pady=10)
        ttk.Button(self.root, text="🔙 Back", command=self.main_menu).pack()

    def customer_dashboard(self):
        self.clear_screen()
        ttk.Label(self.root, text="👨‍🍽️ Order Your Meal", style="Header.TLabel").pack(pady=20)

        if not self.items_list:
            ttk.Label(self.root, text="No items available yet.").pack()
        else:
            for item in self.items_list:
                ttk.Button(
                    self.root,
                    text=f"🛒 {item['recipe']} — ${item['price']:.2f}",
                    command=lambda i=item: self.add_to_order(i)
                ).pack(pady=3)

        ttk.Button(self.root, text="🧾 View Bill", command=self.view_bill).pack(pady=10)
        ttk.Button(self.root, text="💳 Checkout", command=self.checkout).pack(pady=5)
        ttk.Button(self.root, text="🔙 Back", command=self.main_menu).pack(pady=10)

    def add_to_order(self, item):
        self.order_items.append(item)
        messagebox.showinfo("Added", f"{item['recipe']} added to order!")

    def view_bill(self):
        self.clear_screen()
        ttk.Label(self.root, text="🧾 Your Bill", style="Header.TLabel").pack(pady=20)

        total = 0
        for item in self.order_items:
            ttk.Label(self.root, text=f"{item['recipe']} - ${item['price']:.2f}").pack()
            total += item['price']

        ttk.Label(self.root, text=f"Total: ${total:.2f}", font=("Segoe UI", 14, "bold")).pack(pady=10)
        ttk.Button(self.root, text="🔙 Back", command=self.customer_dashboard).pack()

    def checkout(self):
        if not self.order_items:
            messagebox.showinfo("No Order", "Your cart is empty.")
            return
        total = sum(item['price'] for item in self.order_items)
        self.order_items.clear()
        messagebox.showinfo("Checkout Complete", f"Thanks for ordering!\nTotal: ${total:.2f}")

# ---------------- Run App ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()
