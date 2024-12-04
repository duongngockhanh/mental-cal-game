import random
import time
import tkinter as tk
from tkinter import messagebox

class MentalCal:
    def __init__(self, root):
        self.root = root
        self.root.title("Mental Cal")

        # Initial prompt before starting the game
        self.label_problem = tk.Label(self.root, text="Start to show 1st cal", font=("Arial", 16))
        self.label_problem.pack(pady=20)

        # Timer
        self.timer_label = tk.Label(self.root, text="Time: 0.00", font=("Arial", 12))
        self.timer_label.pack()

        # Timer start flag
        self.timer_running = False
        self.start_time = 0

        # Input field for the answer
        self.answer_entry = tk.Entry(self.root, font=("Arial", 14))
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", self.check_answer)  # Enter key to submit

        # Start button
        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack(pady=10)

    def start_game(self):
        """Start the game and the timer."""
        self.num1 = random.randint(10, 99)
        self.num2 = random.randint(10, 99)
        self.label_problem.config(text=f"What is {self.num1} x {self.num2}?")  # Show the first calculation
        self.answer_entry.delete(0, tk.END)  # Clear previous input
        self.timer_label.config(text="Time: 0.00")
        self.timer_running = True
        self.start_time = time.time()  # Record the start time
        self.update_timer()

    def update_timer(self):
        """Update the timer every 100 ms."""
        if self.timer_running:
            elapsed_time = time.time() - self.start_time  # Get the elapsed time
            self.timer_label.config(text=f"Time: {elapsed_time:.2f}")  # Format to 2 decimal places
            self.root.after(100, self.update_timer)  # Update every 100ms

    def check_answer(self, event=None):
        """Check if the answer is correct."""
        # Stop the timer immediately when the user presses Enter
        self.timer_running = False

        try:
            user_answer = int(self.answer_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
            return

        correct_answer = self.num1 * self.num2
        elapsed_time = float(self.timer_label.cget("text").split(": ")[1])  # Get elapsed time

        # Determine if the answer is correct or incorrect
        if user_answer == correct_answer:
            self.show_custom_message("Correct!", f"You took {elapsed_time:.2f} seconds.", "green")
        else:
            self.show_custom_message("Incorrect!", f"The correct answer is {correct_answer}.", "red")

    def show_custom_message(self, result, message, color):
        """Display a custom message with colored 'correct' or 'incorrect' text."""
        # Create a new window to show the result
        result_window = tk.Toplevel(self.root)
        result_window.title("Result")
        
        # Set a background color for the window
        result_window.configure(bg="white")

        # Display the result message
        result_label = tk.Label(result_window, text=message, font=("Arial", 14), fg=color, bg="white")
        result_label.pack(pady=20)

        # Display the word 'Correct!' or 'Incorrect!' in a colored text
        result_word = tk.Label(result_window, text=result, font=("Arial", 16, "bold"), fg=color, bg="white")
        result_word.pack(pady=10)

        # Close button for the result window
        close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
        close_button.pack(pady=10)

# Create the main window
root = tk.Tk()
game = MentalCal(root)
root.mainloop()
