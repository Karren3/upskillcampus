SQL Scripts for Quiz Game
1. Create Users Table

CREATE TABLE Users (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Username VARCHAR(50) UNIQUE NOT NULL,
    Password VARCHAR(50) NOT NULL
);

2. Create Questions Table

CREATE TABLE Questions (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Category VARCHAR(50),
    Question TEXT,
    OptionA VARCHAR(100),
    OptionB VARCHAR(100),
    OptionC VARCHAR(100),
    OptionD VARCHAR(100),
    CorrectOption CHAR(1)
);

3. Create Leaderboard Table

CREATE TABLE Leaderboard (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Username VARCHAR(50),
    Score INT,
    DateTaken DATETIME DEFAULT GETDATE()
);

4. Sample Data Insert - Questions

INSERT INTO Questions (Category, Question, OptionA, OptionB, OptionC, OptionD, CorrectOption)
VALUES 
('science', 'What planet is known as the Red Planet?', 'Earth', 'Mars', 'Jupiter', 'Venus', 'B'),
('science', 'What gas do plants absorb?', 'Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Hydrogen', 'B'),
('science', 'What's the main source of energy for earth?', 'Moon', 'Star', 'Sun', 'Planets', 'C'),
('science', 'What part of the human body pumps blood?', 'Lung', 'Heart', 'Kidney', 'Liver', 'B'),
('math', 'What is 12 * 12?', '144', '124', '154', '134', 'A'),
('math', 'What is the square root of 64?', '6', '8', '7', '9', 'B'),
('math', 'How many sides does a octogon have?', '7', '9', '5', '8', 'D'),
('math', 'What is the cube root of 8?', '2', '8', '10', '1', 'A'),
('history', 'Who was the first President of the USA?', 'Lincoln', 'Jefferson', 'Washington', 'Adams', 'C'),
('history', 'Who discovered America?', 'Christopher Columbus', 'Neil Armstrong', 'Isaac Newton', 'George Washington', 'A'),
('history', 'Which ancient civilization built the pyramids?', 'Romans', 'Greeks', 'Chinese','Egyptians', 'D'),
('history', 'In which year did World War II end?', '1945', '1942', '1939', '1950', 'A');

