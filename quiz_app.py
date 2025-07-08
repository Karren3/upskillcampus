import tkinter as tk
from tkinter import messagebox
import json
import random
import os

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        self.score = 0
        self.q_index = 0
        self.questions = self.load_questions()

        if not self.questions:
            messagebox.showerror("Error", "No questions loaded. Check questions.json.")
            self.root.destroy()
            return

        random.shuffle(self.questions)

        self.question_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=450, pady=20)
        self.question_label.pack()

        self.var = tk.StringVar()
        self.options = []
        for _ in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.var, value="", font=("Helvetica", 12),
                                 anchor='w', justify='left', wraplength=400)
            btn.pack(fill='x', padx=50, pady=4)
            self.options.append(btn)

        self.next_btn = tk.Button(root, text="Next", command=self.next_question,
                                  font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.next_btn.pack(pady=20)

        self.display_question()

    def load_questions(self):
        filename = "questions.json"
        if not os.path.exists(filename):
            messagebox.showerror("Error", f"File '{filename}' not found.")
            return []

        try:
            with open(filename, "r") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    raise ValueError("JSON content must be a list of questions.")
                return data
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load questions:\n{e}")
            return []

    def display_question(self):
        if self.q_index < len(self.questions):
            q = self.questions[self.q_index]
            self.var.set(None)
            self.question_label.config(text=f"Q{self.q_index + 1}: {q['question']}")
            options = q["options"].copy()
            random.shuffle(options)
            for i in range(4):
                self.options[i].config(text=options[i], value=options[i])
        else:
            self.show_result()

    def next_question(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("No Selection", "Please choose an option before proceeding.")
            return

        correct = self.questions[self.q_index]["answer"]
        if selected == correct:
            self.score += 1

        self.q_index += 1
        self.display_question()

    def show_result(self):
        messagebox.showinfo("Quiz Complete", f"Your score: {self.score} / {len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
