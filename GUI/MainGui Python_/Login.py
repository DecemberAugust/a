import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import pymysql
import sys
python_excutable = sys.executable
# connect to the database
db = pymysql.connect(host='localhost',
                     user='root',
                     password='Haonan02',
                     database='res')
cursor = db.cursor()
def login():
    username = entry_username.get()
    password = entry_password.get()
    remember = check_remember.get()
    # check the username and password from the database
    sql = "SELECT * FROM login WHERE username=%s AND password=%s"
    cursor.execute(sql, (username, password))
    result = cursor.fetchone()
    if result:
        # login successiful
        if remember:
            messagebox.showinfo("Login", "Login successful. Remember me checked.")
            subprocess.Popen([python_excutable, "MainGui Python_/MainGUI_page.py"])
        else:
            messagebox.showinfo("Login", "Login successful. Remember me not checked.")
            subprocess.Popen([python_excutable, "MainGui Python_/MainGUI_page.py"])
    else:
        # login loss
        messagebox.showerror("Error", "Invalid username or password")
        subprocess.Popen([python_excutable, "MainGui Python_/Login.py"])
    db.close()

def main():
    root.destroy()
    subprocess.Popen([python_excutable, "MainGui Python_/signup.py"])
    print("Opening Main Page...")

# Create the main window
root = tk.Tk()
root.title("Technology Studio")
root.geometry("350x600")
root.configure(bg="#263238")

# Create a frame for the content
frame = tk.Frame(root, bg="#263238", padx=40, pady=40)
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
label_title = tk.Label(frame, text="Log in", bg="#263238", fg="orange", font=("Arial", 14, "bold"))
label_title.pack()

# Add more space between button and window 
label_empty = tk.Label(frame, bg="#263238")
label_empty.pack()

# Create username label and entry
label_username = tk.Label(frame, text="Username:", bg="#263238", fg="white")
label_username.pack()
entry_username = tk.Entry(frame, bg="gray")
entry_username.pack()

# Create password label and entry
label_password = tk.Label(frame, text="Password:", bg="#263238", fg="white")
label_password.pack()
entry_password = tk.Entry(frame, bg="gray", show="*")
entry_password.pack()

# Create "Remember me" checkbox
check_remember = tk.IntVar()
checkbox_remember = tk.Checkbutton(frame, text="Remember me", variable=check_remember, bg="#263238", fg="white")
checkbox_remember.pack()

# Add more space between button and window 
label_empty = tk.Label(frame, bg="#263238")
label_empty.pack()

# Create login button
button_login = tk.Button(frame, text="Login", bg="grey", fg="white", command=login)
button_login.pack()

# Add more space between button and window 
label_empty = tk.Label(frame, bg="#263238")
label_empty.pack()

# Create signup button
button_signup = tk.Button(frame, text="Sign up", bg="grey", fg="white", command=main)
button_signup.pack()

# Start the main loop
root.mainloop()