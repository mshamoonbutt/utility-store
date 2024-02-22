from tkinter import *
from tkinter import messagebox

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

    Button(root, text="Logout", width=9, pady=2, bg="yellow", fg="black", border=0, command=logout_profile).place(x=25, y=10)


    root.mainloop()
###################################################################
#Store Page 
# Function to open a new page for each category
def open_category_page(category):
    messagebox.showinfo("Category", f"You clicked on {category}")

# Function to open the grocery page
def open_grocery_page():
    def add_to_cart(product):
        with open("cart.txt", "a") as file:
            file.write(f"{product}\n")
        messagebox.showinfo("Cart", "Added to cart successfully")

    grocery_window = Toplevel()
    grocery_window.title("Grocery")
    grocery_window.geometry("400x300")
    grocery_window.config(bg="black")
    Label(grocery_window, text="Welcome to the Grocery Page", font=("Arial", 18), bg="black", fg="yellow").pack(pady=20)
    # Add button to add product to cart
    Button(grocery_window, text="Add to Cart", bg="yellow", fg="black", command=lambda: add_to_cart("Grocery Product")).pack(pady=10)
    # You can add more widgets and functionality to this page as needed

# Function to open the plastic page
def open_plastic_page():
    def add_to_cart(product):
        with open("cart.txt", "a") as file:
            file.write(f"{product}\n")
        messagebox.showinfo("Cart", "Added to cart successfully")    
    
    plastic_window = Toplevel()
    plastic_window.title("Plastic")
    plastic_window.geometry("400x300")
    plastic_window.config(bg="black")
    Label(plastic_window, text="Welcome to the Plastic Page", font=("Arial", 18), bg="black", fg="yellow").pack(pady=20)
    
    Button(plastic_window, text="Add to Cart", bg="yellow", fg="black", command=lambda: add_to_cart("Plastic Product")).pack(pady=10)

# Function to open the clothes page
def open_clothes_page():
    def add_to_cart(product):
        with open("cart.txt", "a") as file:
            file.write(f"{product}\n")
        messagebox.showinfo("Cart", "Added to cart successfully")    
    
    clothes_window = Toplevel()
    clothes_window.title("Clothes")
    clothes_window.geometry("400x300")
    clothes_window.config(bg="black")
    Label(clothes_window, text="Welcome to the Clothes Page", font=("Arial", 18), bg="black", fg="yellow").pack(pady=20)
    Button(clothes_window, text="Add to Cart", bg="yellow", fg="black", command=lambda: add_to_cart("Clothes")).pack(pady=10)

# Function to open the meat page
def open_meat_page():
    def add_to_cart(product):
        with open("cart.txt", "a") as file:
            file.write(f"{product}\n")
        messagebox.showinfo("Cart", "Added to cart successfully")    
    
    meat_window = Toplevel()
    meat_window.title("Meat")
    meat_window.geometry("400x300")
    meat_window.config(bg="black")
    Label(meat_window, text="Welcome to the Meat Page", font=("Arial", 18), bg="black", fg="yellow").pack(pady=20)
    Button(meat_window, text="Add to Cart", bg="yellow", fg="black", command=lambda: add_to_cart("Meat")).pack(pady=10)
# Function to open the vegetables page
def open_vegetables_page():
    def add_to_cart(product):
        with open("cart.txt", "a") as file:
            file.write(f"{product}\n")
        messagebox.showinfo("Cart", "Added to cart successfully")    
    
    vegetables_window = Toplevel()
    vegetables_window.title("Vegetables")
    vegetables_window.geometry("400x300")
    vegetables_window.config(bg="black")
    Label(vegetables_window, text="Welcome to the Vegetables Page", font=("Arial", 18), bg="black", fg="yellow").pack(pady=20)
    Button(vegetables_window, text="Add to Cart", bg="yellow", fg="black", command=lambda: add_to_cart("Vegetables")).pack(pady=10)
# Function to open the fruits page
def open_fruits_page():
    def add_to_cart(product):
        with open("cart.txt", "a") as file:
            file.write(f"{product}\n")
        messagebox.showinfo("Cart", "Added to cart successfully")    
    
    fruits_window = Toplevel()
    fruits_window.title("Fruits")
    fruits_window.geometry("400x300")
    fruits_window.config(bg="black")
    Label(fruits_window, text="Welcome to the Fruits Page", font=("Arial", 18), bg="black", fg="yellow").pack(pady=20)
    Button(fruits_window, text="Add to Cart", bg="yellow", fg="black", command=lambda: add_to_cart("Fruits")).pack(pady=10)
# Function to create the store page
def store():
    def add_to_cart(product):
        with open("cart.txt", "a") as file:
            file.write(f"{product}\n")
        messagebox.showinfo("Cart", f"Added {product} to cart successfully")

    def add_to_cart_dropdown(product, frame):
        add_to_cart(product)
        frame.destroy()

    root = Tk()
    root.title("Shop")
    root.geometry("925x750+250+0")
    root.config(bg="black")
    root.resizable(False, False)

    # Create frames for different categories
    grocery_frame = Frame(root, width=200, height=700, bg="black")
    grocery_frame.place(x=80, y=100)
    plastic_frame = Frame(root, width=200, height=700, bg="black")
    plastic_frame.place(x=400, y=100)
    clothes_frame = Frame(root, width=200, height=700, bg="black")
    clothes_frame.place(x=700, y=100)
    meat_frame = Frame(root, width=200, height=700, bg="black")
    meat_frame.place(x=80, y=400)
    vegetables_frame = Frame(root, width=200, height=700, bg="black")
    vegetables_frame.place(x=400, y=400)
    fruits_frame = Frame(root, width=200, height=700, bg="black")
    fruits_frame.place(x=700, y=400)

    # Add buttons to the frames with dropdown menu
    def create_dropdown(frame, product_list):
        menu_var = StringVar(frame)
        menu_var.set("Select Product")

        dropdown_menu = OptionMenu(frame, menu_var, *product_list)
        dropdown_menu.pack(pady=5)

        quantity_label = Label(frame, text="Quantity:", bg="black", fg="yellow")
        quantity_label.pack(pady=5)
        quantity_entry = Entry(frame, width=10, bg="lightgray")
        quantity_entry.pack(pady=5)

        def add_to_cart_with_quantity():
            product = menu_var.get()
            quantity = quantity_entry.get()
            if product and quantity:
                with open("cart.txt", "a") as file:
                    file.write(f"{product} (Quantity: {quantity})\n")
                messagebox.showinfo("Cart", f"Added {quantity} {product}(s) to cart successfully")
            else:
                messagebox.showerror("Error", "Please select a product and enter a quantity.")

        Button(frame, text="Add to Cart", bg="yellow", fg="black", command=add_to_cart_with_quantity).pack(pady=10)


    def open_grocery_page():
        create_dropdown(grocery_frame, ["Milk", "Wheat", "Eggs", "Sugar"])

    def open_plastic_page():
        create_dropdown(plastic_frame, ["Chair", "Table", "Cutlery"])

    def open_clothes_page():
        create_dropdown(clothes_frame, ["Men", "Women", "Kids"])

    def open_meat_page():
        create_dropdown(meat_frame, ["Chicken", "Fish", "Goat"])

    def open_vegetables_page():
        create_dropdown(vegetables_frame, ["Potato", "Peas", "Tomato"])

    def open_fruits_page():
        create_dropdown(fruits_frame, ["Apple", "Banana", "Peach"])
        
    def search_movies():
        pass

    Button(grocery_frame, text="Grocery", bg="black", fg="yellow", font=("Arial", 14, "bold"), command=open_grocery_page).pack(pady=10)
    Button(plastic_frame, text="Plastic", bg="black", fg="yellow", font=("Arial", 14, "bold"), command=open_plastic_page).pack(pady=10)
    Button(clothes_frame, text="Clothes", bg="black", fg="yellow", font=("Arial", 14, "bold"), command=open_clothes_page).pack(pady=10)
    Button(meat_frame, text="Meat", bg="black", fg="yellow", font=("Arial", 14, "bold"), command=open_meat_page).pack(pady=10)
    Button(vegetables_frame, text="Vegetables", bg="black", fg="yellow", font=("Arial", 14, "bold"), command=open_vegetables_page).pack(pady=10)
    Button(fruits_frame, text="Fruits", bg="black", fg="yellow", font=("Arial", 14, "bold"), command=open_fruits_page).pack(pady=10)
    Button(root, text="Logout", width=9, pady=2, bg="yellow", fg="black", border=0, command=logout_store).place(x=25, y=10)
    Button(root, text='Search', command=search_movies, bg='yellow', fg='black').place(x=850, y=10)  # Adjusted position


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