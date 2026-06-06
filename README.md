# Revision-Tool
A quick and easy revision program allowing you to input questions & answers for quizzes and flashcards.
# What is this?
A simple revision-focused application built in Python to help users practise their own questions and answers.

## Features
- Allows users to input their own questions and answers into 5 different documents which can later be updated
- Users can choose between Quiz mode or Flashcard mode
- Quiz mode gives users three attempts to answer a randomly selected question
- Flashcard mode displays a random question and allows users to flip the card to view the answer

## Requirements
- Python 3
- Custom TKinter

## Why I built this
I built this project to help with my A Level revision so I could simply create and practise questions on topics from class

## Future improvements
- Allow users to label questions as "confident" or "needs practise" for Quiz and Flashcards
- Support multiple Q&A documents so users can create and organise questions by topic

## How to install CustomTKinter
- In Command Promp (Windows) or Terminal (macOS/Linux), run "pip install customtkinter"
    - If pip is not recognised try running:
        "python -m pip install customtkinter" or "py -m pip install customtkinter"
- If that still doesn’t work, ensure Python is installed and added to PATH or find further tutorials for this process online

## How to run
Run the main python file after installing CustomTkinter and Python 3 - This can be done by double clicking the MainProgram.py file in the folder

## How to use
- Click the "Questions & Answers" button at the top and a menu with a text box should appear. In that  text box, write a question in the top line and the answer to that question the line below it. This can then be repeated with every odd line being a question and every even one being answers.
- Once all questions and answers have been written, click "Save Questions" and then close and re-open the program again to update the program for the new questions.
- In the quiz section a question will appear, then you need to write an answer in the text box. Once you have written the question, click "submit" and it will display if you got it wrong or right. You can then click "Next Question" to load the next one.
- In the flashcards section a question will appear and you can click "flip" to see the answer and then "Next Question" to show the next flashcard