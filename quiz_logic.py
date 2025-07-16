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
