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


