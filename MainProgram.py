# Made with Python using CustomTKinter for GUI
# Imports
import random
import os
import customtkinter as ctk


# CustomTKinter GUI Design and Layout
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Revision Tool")
root.geometry("1200x800")


# Everything Under Top Bar
All = ctk.CTkFrame(root)
All.pack(fill="both", expand=True)

# Top bar
bar = ctk.CTkFrame(root, fg_color="transparent")
bar.place(x=0, y=0, relwidth=1, heigh=50)

quizButton = ctk.CTkButton(bar, text="Quiz")
quizButton.pack(side="left", pady=0, padx=10)

fCardButton = ctk.CTkButton(bar, text="Flashcards")
fCardButton.pack(side="left", pady=0, padx=0)

qListButton = ctk.CTkButton(bar, text="Questions & Answers")
qListButton.pack(side="left", pady=0, padx=50)

# Quiz frame
QA = ctk.CTkFrame(All, fg_color="transparent") # Question and Answer Frame
QA.place(x=0, y=100, relwidth=1, relheight=1)

Question = ctk.CTkLabel(QA, text="Loading Question", font=("Arial Bold", 30), wraplength=520) # Question text
Question.pack(padx=20, pady=(20, 10))

answerBox = ctk.CTkTextbox(QA, width=750, height=200, font=("Calibri", 18)) # Answer text box
answerBox.pack(pady=(10, 50), padx=20)

submitButton = ctk.CTkButton(QA, text="Submit") # Submit Button
submitButton.pack(pady=5)

result = ctk.CTkLabel(QA, text="", font=("Arial", 18)) # Result text below Submit Button
result.pack(padx=20,pady=0)

# Flashcard front frame
FCfront = ctk.CTkFrame(All, fg_color="transparent")

fQuestion = ctk.CTkLabel(FCfront, text="Loading Question", font=("Arial", 50), wraplength=750, fg_color="black", text_color="white") # Question text
fQuestion.pack(padx=0, pady=0)

flipButton = ctk.CTkButton(FCfront, text="make this say nothing")
flipButton.pack(padx=0, pady=45)

# Flashcard back frame
FCback = ctk.CTkFrame(All, fg_color="transparent")

bQuestion = ctk.CTkLabel(FCback, text="Loading Answer", font=("Arial", 50), wraplength=750, fg_color="black", text_color="white") # Question text
bQuestion.pack(padx=0, pady=0)

BflipButton = ctk.CTkButton(FCback, text="make this say nothing")
BflipButton.pack(padx=0, pady=45)

nextQ = ctk.CTkButton(FCback, text="make this say something")
nextQ.pack(padx=0, pady=45)

# Question & Answer Document 1
docuFrame1 = ctk.CTkFrame(All, fg_color="transparent")

titleText1 = ctk.CTkLabel(docuFrame1, text="Questions & Answers Document", font=("Arial", 40), text_color="white")
titleText1.pack(pady=0)

docuText1 = ctk.CTkTextbox(docuFrame1, width=800, height=500)
docuText1.pack(pady=10)

saveButton = ctk.CTkButton(docuFrame1, text="Save Questions")
saveButton.pack(pady=20)


# Global Variables
attempts = 0

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "Question & Answers.txt")
f = open(file_path, "r")
lines = f.readlines()


# Subroutines
# Saves written questions and answers to the text document 1
def saveQuestions1():
    content = docuText1.get("1.0", "end").strip()
    f = open(file_path, "w", encoding="utf-8")
    f.write(content)
    getQ()

# Removes quiz GUI and shows Question & Answer GUI
def showDoc1():
     QA.place_forget()
     FCfront.place_forget()
     docuFrame1.place(x=0, y=100, relwidth=1, relheight=1)

     f = open(file_path, "r", encoding="utf-8")
     content = f.read()
     f.close

     docuText1.delete("1.0", "end")
     docuText1.insert("1.0", content)

# Removes previous GUI and opens Quiz GUI
def showQuiz():
     docuFrame1.place_forget()
     FCfront.place_forget()
     FCback.place_forget()
     QA.place(x=0, y=100, relwidth=1, relheight=1)

# Removes previous GUI and opens Flashcards GUI
def showfCard():
     docuFrame1.place_forget()
     QA.place_forget()
     FCback.place_forget()
     fLoadQ()

# Resets submit button and assigns a random question to num
def getQ():
    global num
    submitButton.configure(text="Submit")
    submitButton.configure(command=quest)
    num = random.randrange(0, len(lines) - 1, 2) # Getting random question
    loadQ()

# Gets a random flashcard question
def fGetQ():
    global num
    num = random.randrange(0, len(lines) - 1, 2) # Getting random question
    fLoadQ()


# Grabbing and loading the question and answer for Flashcards
def fLoadQ():
    global fText, Ans
    FCback.place_forget()
    FCfront.place(x=0, y=125, relwidth=1, relheight=1)

    fText = lines[num].strip() # Grabbing question
    Ans = lines[num + 1].strip().lower() # Grabbing answer
    fQuestion.configure(text=fText) # Adding the Flashcard Question text to fText
    flipButton.configure(text="Flip") # Sets flip button text to say flip
    flipButton.configure(command=fLoadBack) # sets flip button to load the back of flashcard

def fLoadBack():
     docuFrame1.place_forget()
     QA.place_forget()
     FCfront.place_forget()
     FCback.place(x=0, y=125, relwidth=1, relheight=1) # Places back of flashcard frame
     fLoadA()

def fLoadA():
     bQuestion.configure(text=Ans) # Outputs the answer on back of card
     BflipButton.configure(text="Flip") # Resets the flip button to make it show the front of the card again
     BflipButton.configure(command=fLoadQ)
     nextQ.configure(text="Next Question") # Sets up a new button to allow user to get the next flashcard
     nextQ.configure(command=fGetQ)


# Grabbing and loading the question and answer for the Quiz section
def loadQ():
    global Ans, qText, attempts
    attempts = 0 # resetting attempt variable

    qText = (lines[num].strip() + str("?")) # Grabbing question
    Ans = lines[num + 1].strip().lower() # Grabbing answer
    Question.configure(text=qText) # Adding the Question text to qText
    answerBox.delete("1.0", "end") # to clear last input
    result.configure(text="") # Sets result text to be empty

# Allows user to see, answer, and check questions
def quest():
        global attempts
        userAns = answerBox.get("1.0", "end").strip().lower() # sets the user asnwer to what they input into the text box (stripped) with .lower() allowing it to work with any capitalisation
        if userAns == "": # if user does not input any text and submits, result tells them to enter an answer
             result.configure(text="Please type an answer")
             return
        elif userAns != Ans: # if user answer doesn't equal the actual answer, the attempts increase by one, the result lets them know it is wrong and it lets them try again if they have spare attempts
            attempts = attempts + 1
            if attempts == 2:
                result.configure(text="That's not correct. 1 attempt remaining.")
                answerBox.delete("1.0", "end")
                return
            elif attempts == 1:
                result.configure(text="That's not correct. 2 attempts remaining.")
                answerBox.delete("1.0", "end")
                return
            else:
                result.configure(text="\nIncorrect again.\n The actual answer is: " + Ans) # If user gets question wrong with no attempts left, it tells them the answer
                submitButton.configure(text="Next Question", command=getQ)
        else: # If user gets it correct
            result.configure(text="Correct, well done!")
            submitButton.configure(text="Next Question", command=getQ)


# Main Code
getQ()

quizButton.configure(command=showQuiz)
qListButton.configure(command=showDoc1)
fCardButton.configure(command=showfCard)
saveButton.configure(command=saveQuestions1)
root.mainloop()