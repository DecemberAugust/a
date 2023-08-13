import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys

python_excutable = sys.executable

def main():
    root.destroy()
    subprocess.Popen([python_excutable, "MainGui Python_/Main.py"])
    print("Opening Main Page...")
def main1():
    root.destroy()
    subprocess.Popen([python_excutable, "MainGui Python_/Question.py"])
    print("Opening Question Page...")

# Create the main window
root = tk.Tk()
root.title("Technology Studio")
root.geometry("700x570")  # Set size and position

# Load the background image 
background_image = tk.PhotoImage(file="assets/technology.png")

# Create a label to display the background
label_background = tk.Label(root, image=background_image)
label_background.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label for the title
label_title = tk.Label(root, text="Welcome to My GUI!", font=("Arial", 28, "bold"), bg="#263238", fg="white")
label_title.pack(pady=20)

# Create buttons for different actions

Button_Login = tk.Button(root, text="Account", font=("Arial", 14, "bold"), bg="#FF5722", fg="white", command=main)
Button_Login.pack(pady=10)

Button_Question = tk.Button(root, text="Question", font=("Arial", 14, "bold"), bg="#FF5722", fg="white", command=main1)
Button_Question.pack(pady=10)

Button_exit = tk.Button(root, text="Exit", font=("Arial", 14, "bold"), bg="#B71C1C", fg="white", command=root.quit)
Button_exit.pack(pady=10)

# Create a frame for displaying news headlines and image
frame_news = tk.Frame(root, bg="white", padx=10, pady=10)
frame_news.pack(fill=tk.BOTH, expand=True)

# Create a label for the technology news section
label_news_title = tk.Label(frame_news, text="Technology News", font=("Arial", 20, "bold"), bg="#263238", fg="white")
label_news_title.pack(pady=10)

# Create a Listbox to display the news headlines
headline_listbox = tk.Listbox(frame_news, width=60, height=12, font=("Arial", 12))
headline_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Create a Scrollbar for the Listbox
scrollbar = tk.Scrollbar(frame_news, command=headline_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
headline_listbox.config(yscrollcommand=scrollbar.set)

# Populate the Listbox with sample news headlines
news_headlines = [
    "At 15:24 PM on May 30, the United States Space Exploration Technology",
    "company SpaceX Dragon spacecraft carrying two American astronauts was", 
    "successfully launched and flew to the International Space Station by Falcon 9 rocket."
]

news_headlines1 = [
    "Meta has launched Llama 2 on Facebook, a new large-scale language model with up to ",
    "70 billion parameters. The new generative AI system represents a brilliant foray ",
    "into OpenAI, which has shared few details about most AI models, including GPT-3/3.5 and GPT-4."
]

# Insert an empty string to add space between the headlines
headline_listbox.insert(tk.END, "")

# Insert the first set of headlines
for headline in news_headlines:
    headline_listbox.insert(tk.END, headline)

# Insert an empty string to add space between the sets of headlines
headline_listbox.insert(tk.END, "")

# Insert the second set of headlines
for headline in news_headlines1:
    headline_listbox.insert(tk.END, headline)

# Load and display an image related to technology news
technology_image = Image.open("assets/rocket.png")
technology_image = technology_image.resize((100, 100))
technology_image = ImageTk.PhotoImage(technology_image)
image_label = tk.Label(frame_news, image=technology_image)
image_label.pack(pady=10, side=tk.TOP)

# Load and display an image related to technology news
technology_image1 = Image.open("assets/Meta.png")
technology_image1 = technology_image1.resize((100, 100))
technology_image1 = ImageTk.PhotoImage(technology_image1)
image_label = tk.Label(frame_news, image=technology_image1)
image_label.pack(pady=10, side=tk.TOP)

# Start the main loop
root.mainloop()