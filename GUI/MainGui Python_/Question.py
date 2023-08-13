import tkinter as tk
from tkinter import messagebox
import pymysql
import time
# Sample questions and their options
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Haonan02',
    'database': 'res',
}
countdown = 60
# Global variable to store the list of questions
questions = []
def get_questions_from_db(connection):
    cursor = connection.cursor()

    # Query to select all rows from the questions table
    query = "SELECT * FROM questions"
    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    questions_list = []
    for row in rows:
        questions = {
            "question": row[1],
            "options": [row[2], row[3], row[4], row[5]],
            "correct_answer": row[6]
        }
        questions_list.append(questions)
    cursor.close()
    return questions_list
try:
    connection = pymysql.connect(**config)
    questions_list = get_questions_from_db(connection)
    print(questions_list)
except pymysql.Error as error:
    print("Error: {}".format(error))
finally:
    if 'connection' in locals() and connection.open:
        connection.close()
        print("Database connection closed.")
def check_answers():
    user_answers = [var.get() for var in answer_vars]
    # Check the user's answers against the correct answers
    num_correct_answers = sum(user_answer == question["correct_answer"] for user_answer, question in zip(user_answers, questions_list))
    # Display the result in a message box
    messagebox.showinfo("Result", f"You got {num_correct_answers} out of {len(questions_list)} questions correct!")
def update_countdown():
   global countdown
   # Renew the timer
   countdown -= 1
   label_countdown.config(text=str(countdown))
    
   if countdown > 0:   
      root.after(1000, update_countdown)
   else:
      messagebox.showinfo("Time's Up!", "Time's up!")

# Create the main window
root = tk.Tk()
root.title("Technology Studio")
root.configure(bg="#263238")
# add timer on the top-right
label_countdown = tk.Label(root, text=str(countdown), font=("Arial", 16), anchor="ne")
label_countdown.pack(side="top", pady=10)
# Create a Label for the title
label_title = tk.Label(root, text="Questions", bg="#263238", font=("Arial", 20, "bold"))
label_title.pack(pady=10)

# Create a Frame to hold the questions and options
frame_questions = tk.Frame(root)
frame_questions.pack(pady=10)

# Create variables to store the selected answer for each question
answer_vars = [tk.StringVar() for _ in range(len(questions_list))]

# Create labels and radio buttons for each question and option
for i, question_data in enumerate(questions_list):
    question_label = tk.Label(frame_questions, text=f"{i+1}. {question_data['question']}", font=("Arial", 12))
    question_label.pack(anchor=tk.W)
    for j, option in enumerate(question_data['options']):
        radio_button = tk.Radiobutton(frame_questions, text=option, variable=answer_vars[i], value=option)
        radio_button.pack(anchor=tk.W)

# start timer
update_countdown()
# Create a button to check the answers
button_check_answers = tk.Button(root, text="Check Answers", font=("Arial", 16), command=check_answers)
button_check_answers.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
