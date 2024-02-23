from tkinter import *
from tkinter import messagebox

open_windows = []

# Function to destroy all open windows
def destroy_all_windows():
    for window in open_windows:
        window.destroy()
    open_windows.clear()

#Front page UI
def main_page():
    root = Tk()
    root.title("Home Page")
    root.geometry("925x750+250+0")
    root.config(bg="black")
    root.resizable(False, False)
    frame = Frame(root, width=700, height=700, bg="white")
    frame.place(x=120, y=70)
    heading = Label(root, text="Welcome to Utility Store", fg="yellow", bg="black", font=("Times", 23, "bold"))
    heading.place(x=300, y=10)
    img = PhotoImage(file='image1.png')
    Label(frame, image=img, bg='black').place(x=-2, y=-2)

    # Function to destroy all windows and open the profile page
    def open_profile():
        destroy_all_windows()
        profile()

    # Function to destroy all windows and open the store page
    def open_store():
        destroy_all_windows()
        store()

    # Function to destroy all windows and open the cart page
    def open_cart():
        destroy_all_windows()
        view_cart()

    # Buttons for profile, store, and cart
    Button(root, width=9, pady=2, text="Your Profile", bg="yellow", fg="black", border=0, command=open_profile).place(x=830, y=10)
    Button(root, width=9, pady=2, text="View Store", bg="yellow", fg="black", border=0, command=open_store).place(x=755, y=10)
    Button(root, width=9, pady=2, text="View Cart", bg="yellow", fg="black", border=0, command=open_cart).place(x=25, y=10)

    open_windows.append(root)  # Add the main page window to the list of open windows
    root.mainloop()

#Front page UI
root = Tk()
root.title("Home Page")
root.geometry("925x750+250+0")
root.config(bg="black")
root.resizable(False, False)
frame = Frame(root, width=700, height=700, bg="white")
frame.place(x=120, y=70)
heading = Label(root, text="Welcome to Utility Store", fg="yellow", bg="black", font=("Times", 23, "bold"))
heading.place(x=300, y=10)
img = PhotoImage(file='image1.png')
Label(frame, image=img, bg='black').place(x=-2, y=-2)

#########################################################
def logout_profile():
    root.destroy()  # Close the profile window

def logout_store():
    root.destroy()  # Close the store window
    
def logout():
    # Destroy all open windows
    destroy_all_windows()
    # Open the main page
    main_page()    

#Profile Page View
def profile():
    def login():
        username = login_user.get()
        password = login_pass.get()

        # Read the user details from the file
        with open("user_details.txt", "r") as file:
            for line in file:
                user, pwd = line.strip().split(",")
                if user == username and pwd == password:
                    messagebox.showinfo("Login", "Login successful")  
                    store()  # Open the store page
                    root.destroy() # Close the current window
                    return
        messagebox.showerror("Error", "Invalid username or password")

    def signup():
        username = signup_user.get()
        password = signup_pass.get()
        confirm_password = confirm_pass.get()

        # Check if passwords match
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        # Check password strength
        if not is_strong_password(password):
            messagebox.showerror("Error", "Password is not strong enough, It must c")
            return

        # Write the details to the file
        with open("user_details.txt", "a") as file:
            file.write(f"{username},{password}\n")

        messagebox.showinfo("Signup", "Signup successful")

    # Function to check if password is strong
    def is_strong_password(password):
        # At least 8 characters long
        if len(password) < 8:
            return False
        # Contains at least one uppercase letter
        if not any(char.isupper() for char in password):
            return False
        # Contains at least one lowercase letter
        if not any(char.islower() for char in password):
            return False
        # Contains at least one digit
        if not any(char.isdigit() for char in password):
            return False
        # Contains at least one special character
        if not any(char in '!@#$%^&*()-_+=[]{}|:;"\'<>,.?/~`' for char in password):
            return False
        return True

    root = Tk()
    root.title("Profile")
    root.geometry("925x750+250+0")
    root.config(bg="black")
    root.resizable(False, False)
    frame = Frame(root, width=700, height=700, bg="black")
    frame.place(relx=0.5, rely=0.5, anchor="center")
    heading = Label(root, text="Sign in or Create an Account", fg="yellow", bg="black", font=("Times", 23, "bold"))
    heading.place(relx=0.5, rely=0.1, anchor="center")
    
    # Login Form
    login_frame = Frame(frame, bg="black")
    login_frame.pack(pady=10)
    Label(login_frame, text="Login", font=("Arial", 14, "bold"), bg="black", fg="yellow").grid(row=0, column=0, columnspan=2)
    Label(login_frame, text="Username", bg="black", fg="yellow").grid(row=1, column=0, padx=10, pady=5)
    Label(login_frame, text="Password", bg="black", fg="yellow").grid(row=2, column=0, padx=10, pady=5)
    login_user = Entry(login_frame, width=30, bg="lightgray")
    login_user.grid(row=1, column=1, padx=10, pady=5)
    login_pass = Entry(login_frame, width=30, bg="lightgray", show="*")
    login_pass.grid(row=2, column=1, padx=10, pady=5)
    Button(login_frame, text="Login", width=10, bg="yellow", fg="black", command=login).grid(row=3, column=0, columnspan=2, pady=10)
    
    # Signup Form
    signup_frame = Frame(frame, bg="black")
    signup_frame.pack(pady=10)
    Label(signup_frame, text="Signup Details", font=("Arial", 14, "bold"), bg="black", fg="yellow").grid(row=0, column=0, columnspan=2)
    Label(signup_frame, text="Username", bg="black", fg="yellow").grid(row=1, column=0, padx=10, pady=5)
    Label(signup_frame, text="Password", bg="black", fg="yellow").grid(row=2, column=0, padx=10, pady=5)
    Label(signup_frame, text="Confirm Password", bg="black", fg="yellow").grid(row=3, column=0, padx=10, pady=5)
    signup_user = Entry(signup_frame, width=30, bg="lightgray")
    signup_user.grid(row=1, column=1, padx=10, pady=5)
    signup_pass = Entry(signup_frame, width=30, bg="lightgray", show="*")
    signup_pass.grid(row=2, column=1, padx=10, pady=5)
    confirm_pass = Entry(signup_frame, width=30, bg="lightgray", show="*")
    confirm_pass.grid(row=3, column=1, padx=10, pady=5)
    Button(signup_frame, text="Signup", width=10, bg="yellow", fg="black", command=signup).grid(row=4, column=0, columnspan=2, pady=10)

    Button(root, text="Logout", width=9, pady=2, bg="yellow", fg="black", border=0, command=logout).place(x=25, y=10)


    def logout_profile():
        destroy_all_windows()
        main_page()

    Button(root, text="Logout", width=9, pady=2, bg="yellow", fg="black", border=0, command=logout_profile).place(x=25, y=10)

    open_windows.append(root)  # Add the profile page window to the list of open windows

###################################################################
#Store Page 

def store():
    def add_to_cart(product):
        with open("cart.txt", "a") as file:
            file.write(f"{product}\n")
        messagebox.showinfo("Cart", f"Added {product} to cart successfully")

    def add_to_cart_dropdown(product, frame):
        add_to_cart(product)
        frame.destroy()

    def search_product():
        query = search_entry.get()
        filtered_products = [product for product in products if query.lower() in product["product_name"].lower()]
        display_products(filtered_products)

    def sort_products_by_price():
        sorted_products = sorted(products, key=lambda x: x["price"])
        display_products(sorted_products)  
        
    def sort_products_by_price():
        sorted_products = sorted(products, key=lambda x: x["price"])
        display_products(sorted_products)
        

    def add_to_cart(product_name, quantity):
        with open("cart.txt", "a") as file:
            file.write(f"{product_name},{quantity}\n")
        messagebox.showinfo("Cart", f"Added {quantity} {product_name}(s) to cart successfully")

    def add_to_cart_dropdown(product_name, quantity, frame):
        add_to_cart(product_name, quantity)
        frame.destroy()

    def display_products(product_list):
        # Clear the existing products displayed on the screen
        for widget in frame.winfo_children():
            widget.destroy()

        canvas = Canvas(frame, height=650)  # Adjust the height of the canvas
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        inner_frame = Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor='nw')

        for i, product in enumerate(product_list):
            product_label = Label(inner_frame, text=f"{product['product_name']} - ${product['price']}", bg="black", fg="white", font=("Arial", 12))
            product_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            quantity_entry = Entry(inner_frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            add_to_cart_button = Button(inner_frame, text="Add to Cart", bg="yellow", fg="black", command=lambda p=product, q=quantity_entry: add_to_cart_dropdown(p["product_name"], q.get(), inner_frame))
            add_to_cart_button.grid(row=i, column=2, padx=10, pady=5)

        inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))




    root = Tk()
    root.title("Shop")
    root.geometry("925x750+250+0")
    root.config(bg="black")
    root.resizable(False, False)

    frame = Frame(root, width=700, height=700, bg="white")
    frame.place(x=120, y=70)

    # Read products from file
    products = []
    with open("products.txt", "r") as file:
        for line in file:
            product_data = line.strip().split(",")
            product = {
                "product_name": product_data[0],
                "category": product_data[1],
                "price": float(product_data[2]),
                "quantity_in_stock": int(product_data[3])
            }
            products.append(product)

    # Buttons for searching and sorting
    search_entry = Entry(root, width=30, bg="lightgray")
    search_entry.place(x=120, y=20)
    search_button = Button(root, text="Search", width=10, bg="yellow", fg="black", command=search_product)
    search_button.place(x=350, y=18)
    sort_button = Button(root, text="Sort by Price", width=15, bg="yellow", fg="black", command=sort_products_by_price)
    sort_button.place(x=450, y=18)

    display_products(products)

    root.mainloop()


def view_cart():
    def remove_item(item):
        # Read the cart items from the file
        cart_items = []
        try:
            with open("cart.txt", "r") as file:
                for line in file:
                    if line.strip() != item:
                        cart_items.append(line.strip())
        except FileNotFoundError:
            pass  # If the cart file does not exist, ignore and proceed with an empty cart

        # Write the updated cart items back to the file
        with open("cart.txt", "w") as file:
            for cart_item in cart_items:
                file.write(f"{cart_item}\n")

        # Refresh the cart window
        cart_window.destroy()
        view_cart()

    cart_window = Toplevel()
    cart_window.title("View Cart")
    cart_window.geometry("400x300")
    cart_window.config(bg="black")

    cart_items = []
    try:
        # Read the cart items from the file
        with open("cart.txt", "r") as file:
            for line in file:
                cart_items.append(line.strip())
    except FileNotFoundError:
        pass  # If the cart file does not exist, ignore and proceed with an empty cart

    if cart_items:
        Label(cart_window, text="Your Cart Items:", font=("Arial", 18), bg="black", fg="yellow").pack(pady=10)
        for item in cart_items:
            frame = Frame(cart_window, bg="black")
            frame.pack(fill="x")
            Label(frame, text=item, bg="black", fg="white", width=20).pack(side="left", padx=5)
            Button(frame, text="Remove", bg="red", fg="white", command=lambda i=item: remove_item(i)).pack(side="right", padx=5)
    else:
        Label(cart_window, text="Your cart is empty.", font=("Arial", 18), bg="black", fg="yellow").pack(pady=10)



# Buttons for profile, store, and \undefined
Button(root, width=9, pady=2, text="Your Profile", bg="yellow", fg="black", border=0, command=profile).place(x=830, y=10)
Button(root, width=9, pady=2, text="View Store", bg="yellow", fg="black", border=0, command=store).place(x=755, y=10)
Button(root, width=9, pady=2, text="View Cart", bg="yellow", fg="black", border=0, command=view_cart).place(x=25, y=10)

root.mainloop()