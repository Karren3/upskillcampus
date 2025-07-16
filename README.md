# upskillcampus
Quiz Game


A simple desktop-based Quiz Game built using Python (Tkinter) and SQL Server. This educational application allows users to register, log in, and test their knowledge in categories like Science, Math, and History.
Features
- User Registration & Login (with credential validation)
- Multiple Quiz Categories: Science, Math, History
- Randomized Questions with Multiple Choice
- Score Evaluation
- Leaderboard Tracking
- SQL Server Integration for persistent storage
- Light-blue GUI with improved layout using Tkinter
- Password hidden in login/register forms
- Input validations and error messages
- Seed default questions automatically if not present
- Easy-to-read interface with improved buttons
- 
  Setup Instructions
Requirements:
- Python 3.8+
- SQL Server (any edition)
- ODBC Driver for SQL Server
- Python Libraries:
  - pyodbc
  - tkinter (usually comes with Python)
    
Install Required Packages
pip install pyodbc

Set Up SQL Server Database
Open SQL Server Management Studio (SSMS) and run the SQL scripts from the provided 'QuizGame_SQL_Scripts.docx' to:
- Create the quizgame database
- Create Users, Questions, and Scores tables
- Insert default questions into each category
Important: Update your Python connection string if your server name is different:
"SERVER=DESKTOP-90CKLJ3;"  # Replace with your actual SQL Server instance name

  Running the Game
1. Make sure your SQL Server service is running.
2. Open quiz_game.py in any Python IDE or text editor.
3. Run the script:
   python quiz_game.py


