def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-90CKLJ3;"  # Replace with your SQL Server
        "DATABASE=quizgame.db;"       # Note: no .db
        "Trusted_Connection=yes;"
    )
