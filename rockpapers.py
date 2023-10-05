import random
import tkinter as tk
from PIL import Image, ImageTk
import time
from ttkthemes import ThemedStyle

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!", 1
    else:
        return "Computer wins!", -1

# Function to handle button clicks
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result, score = determine_winner(user_choice, computer_choice)

    # Update labels and scores
    user_label.config(text=f"You chose {user_choice}")
    result_label.config(text="Thinking...", fg="#FFFFFF")  # Set text color to white
    update_score_labels()
    root.update()

    # Simulate computer's choice with a delay for animation
    time.sleep(1)
    computer_label.config(text=f"Computer chose {computer_choice}")
    result_label.config(text=result, fg="#FFFFFF" if score > 0 else "#FFFFFF")  # Set text color to white

    user_score += score
    computer_score -= score
    update_score_labels()

def update_score_labels():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.configure(bg="#000000")  # Set background color to black

# Load images for rock, paper, and scissors
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png"))

# Create buttons with themed styling
style = ThemedStyle(root)
style.set_theme("breeze")

# Configure button styles
style.configure("TButton",
                font=("Arial", 14, "bold"),
                relief="ridge",
                borderwidth=3,
                foreground="#FFFFFF",  # Set text color to white
                background="#000000",  # Set background color to black
                padx=10,
                pady=10,
                width=10,
                )

rock_button = tk.Button(root, image=rock_img, command=lambda: play("rock"))
paper_button = tk.Button(root, image=paper_img, command=lambda: play("paper"))
scissors_button = tk.Button(root, image=scissors_img, command=lambda: play("scissors"))

# Pack the buttons with padding
rock_button.grid(row=0, column=0, padx=20, pady=10)
paper_button.grid(row=0, column=1, padx=20, pady=10)
scissors_button.grid(row=0, column=2, padx=20, pady=10)

# Create labels for results and scores
user_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#000000", fg="#FFFFFF")  # Set label colors
computer_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#000000", fg="#FFFFFF")  # Set label colors
result_label = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="#000000", fg="#FFFFFF")  # Set label colors
user_score_label = tk.Label(root, text="Your Score: 0", font=("Arial", 14, "bold"), bg="#000000", fg="#FFFFFF")  # Set label colors
computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Arial", 14, "bold"), bg="#000000", fg="#FFFFFF")  # Set label colors

user_label.grid(row=1, column=0, columnspan=3)
computer_label.grid(row=2, column=0, columnspan=3)
result_label.grid(row=3, column=0, columnspan=3)
user_score_label.grid(row=4, column=0, padx=(0, 20), sticky="w")
computer_score_label.grid(row=4, column=2, padx=(20, 0), sticky="e")

# Initialize scores
user_score = 0
computer_score = 0

# Start the GUI event loop
root.mainloop()
