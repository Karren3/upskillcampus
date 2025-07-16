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
