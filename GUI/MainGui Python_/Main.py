import tkinter as tk
import subprocess
import sys
from PIL import Image, ImageTk

python_excutable = sys.executable

def main():
    root.destroy()
    subprocess.Popen([python_excutable, "MainGui Python_/Login.py"])
    print("Opening Login Page...")

def main1():
    root.destroy()
    subprocess.Popen([python_excutable, "MainGui Python_/Signup.py"])
    print("Opening Signup Page...")
# Create the main window
root = tk.Tk()
root.title("Technology Studio")
root.geometry("350x690")
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

# Create labels and buttons
label_title = tk.Label(frame, text="Welcome to the Main Page", fg="orange", bg="#263238")
label_title.pack()

# Add more space between button and window 
label_empty = tk.Label(frame, bg="#263238")
label_empty.pack()

button_login = tk.Button(frame, text="Login", command=main)
button_login.pack()

# Add more space between button and window 
label_empty = tk.Label(frame, bg="#263238")
label_empty.pack()

button_signup = tk.Button(frame, text="Signup", command=main1)
button_signup.pack()

# Start the GUI event loop
root.mainloop()