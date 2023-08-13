import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
import pymysql
import sys

python_excutable = sys.executable
def create_account():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    gender = choice_var.get()
    if gender == "Other":
        custom_gender = entry_custom_gender.get()
        print(f"Username: {username}, Gender: {custom_gender}")
    else:
        print(f"Username: {username}, Gender: {gender}")

    age = entry_age.get()
    mail = entry_gmail.get()

    # Connect to MySQL database
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='Haonan02',
                         database='res')

    cursor = db.cursor()

    # Insert data into register table
    sql = "INSERT INTO register (username, password, confirm_password, gender, age, mail) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (username, password, confirm_password, gender, age, mail)
    cursor.execute(sql, val)

    # Insert username and password into login table
    sql = "INSERT INTO login (username, password, remember) VALUES (%s, %s, %s)"
    val = (username, password, '')
    cursor.execute(sql, val)

    db.commit()
    db.close()
    messagebox.showinfo("Account Created", "Account created successfully.")
    subprocess.Popen([python_excutable, "MainGui Python_/Login.py"])
# Create the main window
root = tk.Tk()
root.title("Technology Studio")
root.geometry("350x690")  # Set size and position
root.configure(bg="#263238") # Background colour

# Create a frame in the middle
frame = tk.Frame(root, padx=70, pady=70)
frame.configure(bg="#263238")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Load the image (replace "logo.png" with your image path)
image = Image.open("assets/logo.png")
image = image.resize((200, 100))
# Convert the image to Tkinter-compatible format
image = ImageTk.PhotoImage(image)

# Create a label to display the image in the top right corner
image_label = tk.Label(frame, image=image, bg="#263238")
image_label.image = image  # Save a reference to avoid garbage collection
image_label.pack(anchor=tk.NE)  # Anchor the label to the top right corner

# Create a title label for the frame
label_title = tk.Label(frame, text="Create New Account", bg="#263238", fg="orange", font=("Arial", 14, "bold"))
label_title.pack()

# Add more space between title and window 
label_empty = tk.Label(frame, bg="#263238")
label_empty.pack()

# Create username label and entry
label_username = tk.Label(frame, text="Name:", bg="#263238", fg="white")
label_username.pack()
entry_username = tk.Entry(frame, bg="#979290")
entry_username.pack()

# Create age label and entry
label_age = tk.Label(frame, text="Age:", bg="#263238", fg="white")
label_age.pack()
entry_age = tk.Entry(frame, bg="#979290")
entry_age.pack()

# Create Email label and entry
label_gmail = tk.Label(frame, text="Email:", bg="#263238", fg="white")
label_gmail.pack()
entry_gmail = tk.Entry(frame, bg="#979290")
entry_gmail.pack()

# Create a label for the choice
label_choice = tk.Label(frame, text="Select your gender:", bg="#263238", fg="white")
label_choice.pack()

# Create a variable to store the selected choice
choice_var = tk.StringVar()

# Create the choice options
choices = ["Male", "Female", "Secret", "Other"]
# Create buttons for each choice
for choice in choices:
    rb_choice = tk.Radiobutton(frame, text=choice, variable=choice_var, value=choice, padx=20, pady=5, bg="#263238", fg="white")
    rb_choice.pack()

# Create an entry for custom gender
entry_custom_gender = tk.Entry(frame, bg="#979290", state=tk.DISABLED)
entry_custom_gender.pack()

# Function to enable the custom gender entry when "Other" is selected
def on_other_selected():
    if choice_var.get() == "Other":
        entry_custom_gender.config(state=tk.NORMAL)
    else:
        entry_custom_gender.config(state=tk.DISABLED)

# Bind the function to the choice_var variable
choice_var.trace("w", lambda *args: on_other_selected())

# Create password label and entry
label_password = tk.Label(frame, text="Password:", bg="#263238", fg="white")
label_password.pack()
entry_password = tk.Entry(frame, bg="#979290", show="*")
entry_password.pack()

# Create confirm password label and entry
label_confirm_password = tk.Label(frame, text="Confirm Password:", bg="#263238", fg="white")
label_confirm_password.pack()
entry_confirm_password = tk.Entry(frame, bg="#979290", show="*")
entry_confirm_password.pack()

# Add more space between button and window 
label_empty = tk.Label(frame, bg="#263238")
label_empty.pack()

# Create create account button
button_account = tk.Button(frame, text="Sign Up", bg="grey", fg="white", command=create_account)
button_account.pack()

# Start the main loop
root.mainloop()