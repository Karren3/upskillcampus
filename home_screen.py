def build_welcome_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Welcome", font=('Arial', 28, 'bold'), bg="#e6f2ff").pack(pady=40)
        tk.Button(self.root, text="Login", width=20, height=2, bg="#4da6ff", fg="white", font=('Arial', 12),
                  command=self.build_actual_login_form).pack(pady=10)
        tk.Button(self.root, text="Register", width=20, height=2, bg="#4da6ff", fg="white", font=('Arial', 12),
                  command=self.build_register_form).pack(pady=10)


