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


