import tkinter as tk
from tkinter import messagebox
import pyodbc

# ---------------- DB CONNECTION ----------------

def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-90CKLJ3;"  # Replace with your SQL Server
        "DATABASE=quizgame.db;"       # Note: no .db
        "Trusted_Connection=yes;"
    )

# ---------------- GUI APP ----------------

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("600x600")
        self.root.configure(bg="#e6f2ff")  # Light blue background
        self.user = None
        self.questions = []
        self.question_index = 0
        self.score = 0
        self.current_category = None

        self.seed_questions_if_needed()
        self.build_welcome_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ------------- WELCOME SCREEN ----------------

    def build_welcome_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Welcome", font=('Arial', 28, 'bold'), bg="#e6f2ff").pack(pady=40)
        tk.Button(self.root, text="Login", width=20, height=2, bg="#4da6ff", fg="white", font=('Arial', 12),
                  command=self.build_actual_login_form).pack(pady=10)
        tk.Button(self.root, text="Register", width=20, height=2, bg="#4da6ff", fg="white", font=('Arial', 12),
                  command=self.build_register_form).pack(pady=10)

    # ------------- LOGIN FORM ----------------

    def build_actual_login_form(self):
        self.clear_window()
        tk.Label(self.root, text="Login", font=('Arial', 24, 'bold'), bg="#e6f2ff").pack(pady=30)

        tk.Label(self.root, text="Username", bg="#e6f2ff").pack()
        self.login_username = tk.Entry(self.root, font=('Arial', 12), width=30)
        self.login_username.pack()

        tk.Label(self.root, text="Password", bg="#e6f2ff").pack()
        self.login_password = tk.Entry(self.root, show='*', font=('Arial', 12), width=30)
        self.login_password.pack()

        tk.Button(self.root, text="Login", bg="#4da6ff", fg="white", width=15,
                  command=self.login_user).pack(pady=10)
        tk.Button(self.root, text="Back", width=10, command=self.build_welcome_screen).pack()

    def login_user(self):
        uname = self.login_username.get().strip()
        pwd = self.login_password.get().strip()
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Users WHERE Username=? AND Password=?", (uname, pwd))
        user = cur.fetchone()
        conn.close()
        if user:
            self.user = uname
            self.show_categories()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials.")

    # ------------- REGISTER ----------------

    def build_register_form(self):
        self.clear_window()
        tk.Label(self.root, text="Register", font=('Arial', 24, 'bold'), bg="#e6f2ff").pack(pady=30)

        tk.Label(self.root, text="Username", bg="#e6f2ff").pack()
        self.reg_username = tk.Entry(self.root, font=('Arial', 12), width=30)
        self.reg_username.pack()

        tk.Label(self.root, text="Password", bg="#e6f2ff").pack()
        self.reg_password = tk.Entry(self.root, show='*', font=('Arial', 12), width=30)
        self.reg_password.pack()

        tk.Button(self.root, text="Register", bg="#4da6ff", fg="white", width=15,
                  command=self.register_user).pack(pady=10)
        tk.Button(self.root, text="Back", width=10, command=self.build_welcome_screen).pack()

    def register_user(self):
        uname = self.reg_username.get().strip()
        pwd = self.reg_password.get().strip()
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO Users (Username, Password) VALUES (?, ?)", (uname, pwd))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful! Please log in.")
            self.build_actual_login_form()
        except pyodbc.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
        finally:
            conn.close()

    # ------------- CATEGORY SCREEN ----------------

    def show_categories(self):
        self.clear_window()
        tk.Label(self.root, text=f"Welcome, {self.user}!", font=('Arial', 20, 'bold'), bg="#e6f2ff").pack(pady=20)
        tk.Label(self.root, text="Select Quiz Category", font=('Arial', 16), bg="#e6f2ff").pack(pady=10)

        for cat in ["science", "math", "history"]:
            tk.Button(self.root, text=cat.capitalize(), width=25, height=2, bg="#0073e6", fg="white",
                      command=lambda c=cat: self.load_questions(c)).pack(pady=5)

        tk.Button(self.root, text="Leaderboard", width=25, height=2, bg="#009933", fg="white",
                  command=self.show_leaderboard).pack(pady=10)

        tk.Button(self.root, text="Logout", bg="gray", fg="white", width=10, command=self.build_welcome_screen).pack(pady=10)

    # ------------- QUIZ LOGIC ----------------

    def load_questions(self, category):
        self.current_category = category
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT Question, OptionA, OptionB, OptionC, OptionD, CorrectOption FROM Questions WHERE Category=?", (category,))
        self.questions = cur.fetchall()
        conn.close()

        if not self.questions:
            messagebox.showinfo("No Questions", f"No questions found in {category}")
            return

        self.question_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        self.clear_window()
        q = self.questions[self.question_index]
        tk.Label(self.root, text=f"Q{self.question_index+1}: {q.Question}", wraplength=500, font=('Arial', 14, 'bold'),
                 bg="#e6f2ff").pack(pady=30)

        self.selected_option = tk.StringVar()
        options = [q.OptionA, q.OptionB, q.OptionC, q.OptionD]
        for i, opt in enumerate(options):
            tk.Radiobutton(self.root, text=opt, variable=self.selected_option, value=chr(65+i),
                           font=('Arial', 12), bg="#e6f2ff").pack(anchor="w", padx=40)

        tk.Button(self.root, text="Submit", bg="#4da6ff", fg="white", command=self.check_answer).pack(pady=20)

    def check_answer(self):
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("No selection", "Please select an answer.")
            return

        correct = self.questions[self.question_index].CorrectOption.strip().upper()
        if selected == correct:
            self.score += 1

        self.question_index += 1
        if self.question_index < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.save_score()
        self.clear_window()
        total = len(self.questions)
        tk.Label(self.root, text="Quiz Complete!", font=('Arial', 18, 'bold'), bg="#e6f2ff").pack(pady=30)
        tk.Label(self.root, text=f"Your Score: {self.score} / {total}", font=('Arial', 16), bg="#e6f2ff").pack(pady=10)

        tk.Button(self.root, text="Back to Categories", width=20, bg="#0073e6", fg="white",
                  command=self.show_categories).pack(pady=10)
        tk.Button(self.root, text="Logout", bg="gray", fg="white", command=self.build_welcome_screen).pack()

    def save_score(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Scores (Username, Category, Score, Total)
            VALUES (?, ?, ?, ?)
        """, (self.user, self.current_category, self.score, len(self.questions)))
        conn.commit()
        conn.close()

    # ------------- LEADERBOARD ----------------

    def show_leaderboard(self):
        self.clear_window()
        tk.Label(self.root, text="Leaderboard", font=('Arial', 20, 'bold'), bg="#e6f2ff").pack(pady=20)

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT TOP 10 Username, Category, Score, Total, DateTaken
            FROM Scores
            ORDER BY Score DESC, DateTaken ASC
        """)
        scores = cur.fetchall()
        conn.close()

        for s in scores:
            display = f"{s.Username} | {s.Category.capitalize()} | {s.Score}/{s.Total} | {s.DateTaken.strftime('%Y-%m-%d')}"
            tk.Label(self.root, text=display, font=('Arial', 12), bg="#e6f2ff").pack()

        tk.Button(self.root, text="Back", bg="gray", fg="white", command=self.show_categories).pack(pady=20)

    # ------------- SEED SAMPLE QUESTIONS ----------------

    def seed_questions_if_needed(self):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("IF NOT EXISTS (SELECT 1 FROM Questions) SELECT 1 ELSE SELECT 0")
        seed_needed = cur.fetchone()[0]

        if seed_needed:
            sample_data = [
                ("science", "What planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", "B"),
                ("science", "What gas do plants absorb?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", "B"),
                ("science", "What's the main source of energy for earth?", "Moon", "Star", "Sun", "Planets", "C"),
                ("science", "What part of the human body pumps blood?", "Lung", "Heart", "Kidney", "Liver", "B"),
                ("math", "What is 12 * 12?", "144", "124", "154", "134", "A"),
                ("math", "What is the square root of 64?", "6", "8", "7", "9", "B"),
                ("math", "How many sides does a octagon have?", "7", "9", "5", "8", "D"),
                ("math", "What is the cube root of 8?", "2", "8", "10", "1", "A"),
                ("history", "Who was the first President of the USA?", "Lincoln", "Jefferson", "Washington", "Adams", "C"),
                ("history", "Who discovered America?", "Christopher Columbus", "Neil Armstrong", "Isaac Newton", "George Washington", "A"),
                ("history", "Which ancient civilization built the pyramids?", "Romans", "Greeks", "Chinese","Egyptians", "D"),
                ("history", "In which year did World War II end?", "1945", "1942", "1939", "1950", "A"),
            ]
            for q in sample_data:
                cur.execute("""
                    INSERT INTO Questions (Category, Question, OptionA, OptionB, OptionC, OptionD, CorrectOption)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, q)
            conn.commit()
        conn.close()


# ---------------- RUN APP ----------------

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
