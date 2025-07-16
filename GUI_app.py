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
