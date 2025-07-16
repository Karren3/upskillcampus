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


