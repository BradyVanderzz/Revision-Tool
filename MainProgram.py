### Made with Python using CustomTKinter for GUI ###
# Imports #
import random
import os
import customtkinter as ctk



# GUI Design and Layout #
# CustomTKinter variable establishment
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
bar.place(relwidth=1, heigh=50)

quizButton = ctk.CTkButton(bar, text="Quiz")
quizButton.pack(side="left", padx=10)

fCardButton = ctk.CTkButton(bar, text="Flashcards")
fCardButton.pack(side="left")

qListButton = ctk.CTkButton(bar, text="Questions & Answers")
qListButton.pack(side="left", padx=50)

# Home Page
HomeP = ctk.CTkFrame(All, fg_color="transparent") # Home page text
HomeP.place(y=125, relwidth=1, relheight=1)

TitleText = ctk.CTkLabel(HomeP, text="Welcome to the Revision Tool!", font=("Arial Black", 60)) # Home page title text
TitleText.pack(padx=20, pady=30)

IntroPara = ctk.CTkLabel(HomeP, text="This application is designed to help you revise.\n\nTo get started, click on the Questions & Answers button on the top bar and input your own questions and answers on every other line, and then do the same for all questions & answers.\nThese questions can then be answered as a quiz or as flashcards.", font=("Arial", 25), wraplength=1050) # Home page introduction paragraph
IntroPara.pack(padx=20, pady=30)

# Quiz frame
QA = ctk.CTkFrame(All, fg_color="transparent") # Question and Answer Frame
QA.place(y=100, relwidth=1, relheight=1)

Question = ctk.CTkLabel(QA, text="Loading Question", font=("Arial Bold", 30), wraplength=520) # Question text
Question.pack(padx=20, pady=(20, 10))

answerBox = ctk.CTkTextbox(QA, width=750, height=200, font=("Calibri", 18)) # Answer text box
answerBox.pack(pady=(10, 50), padx=20)

submitButton = ctk.CTkButton(QA, text="Submit") # Submit Button
submitButton.pack(pady=5)

result = ctk.CTkLabel(QA, text="", font=("Arial", 18)) # Result text below Submit Button
result.pack(padx=20)

# Flashcard front frame
FCfront = ctk.CTkFrame(All, fg_color="transparent")

fQuestion = ctk.CTkLabel(FCfront, text="Loading Question", font=("Arial", 50), wraplength=750, fg_color="black", text_color="white") # Question text
fQuestion.pack()

flipButton = ctk.CTkButton(FCfront, text="make this say nothing")
flipButton.pack(pady=45)

# Flashcard back frame
FCback = ctk.CTkFrame(All, fg_color="transparent")

bQuestion = ctk.CTkLabel(FCback, text="Loading Answer", font=("Arial", 50), wraplength=750, fg_color="black", text_color="white") # Question text
bQuestion.pack()

BflipButton = ctk.CTkButton(FCback, text="make this say nothing")
BflipButton.pack(pady=45)

nextQ = ctk.CTkButton(FCback, text="make this say something")
nextQ.pack(pady=45)

# Questions and Answe Document Home Page
QAhome = ctk.CTkFrame(All, fg_color="transparent")

titleTextQA = ctk.CTkLabel(QAhome, text="Questions & Answers Documents", font=("Arial", 40), text_color="white")
titleTextQA.pack(pady=50)

doc1Button = ctk.CTkButton(QAhome, text="Document 1")
doc1Button.pack(pady=20)

doc2Button = ctk.CTkButton(QAhome, text="Document 2")
doc2Button.pack(pady=20)

doc3Button = ctk.CTkButton(QAhome, text="Document 3")
doc3Button.pack(pady=20)

doc4Button = ctk.CTkButton(QAhome, text="Document 4")
doc4Button.pack(pady=20)

doc5Button = ctk.CTkButton(QAhome, text="Document 5")
doc5Button.pack(pady=20)

# Question & Answer Document 1
docuFrame1 = ctk.CTkFrame(All, fg_color="transparent")

titleText1 = ctk.CTkLabel(docuFrame1, text="Document 1", font=("Arial", 40), text_color="white")
titleText1.pack()

docuText1 = ctk.CTkTextbox(docuFrame1, width=800, height=500)
docuText1.pack(pady=10)

saveButton1 = ctk.CTkButton(docuFrame1, text="Save & Select Questions")
saveButton1.pack(pady=15)

# Question & Answer Document 2
docuFrame2 = ctk.CTkFrame(All, fg_color="transparent")

titleText2 = ctk.CTkLabel(docuFrame2, text="Document 2", font=("Arial", 40), text_color="white")
titleText2.pack()

docuText2 = ctk.CTkTextbox(docuFrame2, width=800, height=500)
docuText2.pack(pady=10)

saveButton2 = ctk.CTkButton(docuFrame2, text="Save & Select Questions")
saveButton2.pack(pady=15)

# Question & Answer Document 3
docuFrame3 = ctk.CTkFrame(All, fg_color="transparent")

titleText3 = ctk.CTkLabel(docuFrame3, text="Document 3", font=("Arial", 40), text_color="white")
titleText3.pack()

docuText3 = ctk.CTkTextbox(docuFrame3, width=800, height=500)
docuText3.pack(pady=10)

saveButton3 = ctk.CTkButton(docuFrame3, text="Save & Select Questions")
saveButton3.pack(pady=15)

# Question & Answer Document 4
docuFrame4 = ctk.CTkFrame(All, fg_color="transparent")

titleText4 = ctk.CTkLabel(docuFrame4, text="Document 4", font=("Arial", 40), text_color="white")
titleText4.pack()

docuText4 = ctk.CTkTextbox(docuFrame4, width=800, height=500)
docuText4.pack(pady=10)

saveButton4 = ctk.CTkButton(docuFrame4, text="Save & Select Questions")
saveButton4.pack(pady=15)

# Question & Answer Document 5
docuFrame5 = ctk.CTkFrame(All, fg_color="transparent")

titleText5 = ctk.CTkLabel(docuFrame5, text="Document 5", font=("Arial", 40), text_color="white")
titleText5.pack()

docuText5 = ctk.CTkTextbox(docuFrame5, width=800, height=500)
docuText5.pack(pady=10)

saveButton5 = ctk.CTkButton(docuFrame5, text="Save & Select Questions")
saveButton5.pack(pady=15)



# Global Variables #
attempts = 0
current_doc = 1  # Track which document is active
last_doc = 1  # Track which document was last selected for quiz/flashcards
num = 0  # Current question index
Ans = ""  # Current answer
qText = ""  # Current question text
fText = ""  # Current flashcard text

base_dir = os.path.dirname(__file__)
fileDoc1 = os.path.join(base_dir, "Document1.txt")
fileDoc2 = os.path.join(base_dir, "Document2.txt")
fileDoc3 = os.path.join(base_dir, "Document3.txt")
fileDoc4 = os.path.join(base_dir, "Document4.txt")
fileDoc5 = os.path.join(base_dir, "Document5.txt")

file_paths = [fileDoc1, fileDoc2, fileDoc3, fileDoc4, fileDoc5]
text_boxes = [docuText1, docuText2, docuText3, docuText4, docuText5]


# Subroutines #
# Helper function to load document lines
def load_document_lines(doc_num):
    file_path = file_paths[doc_num - 1]
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()

lines1 = load_document_lines(1)
lines2 = load_document_lines(2)
lines3 = load_document_lines(3)
lines4 = load_document_lines(4)
lines5 = load_document_lines(5)

# Get active lines based on current document
def get_active_lines():
    return (lines1 if current_doc == 1 else lines2 if current_doc == 2 else
            lines3 if current_doc == 3 else lines4 if current_doc == 4 else lines5)

# Helper to hide all frames
def hide_all_frames():
    QA.place_forget()
    FCfront.place_forget()
    FCback.place_forget()
    HomeP.place_forget()
    QAhome.place_forget()
    docuFrame1.place_forget()
    docuFrame2.place_forget()
    docuFrame3.place_forget()
    docuFrame4.place_forget()
    docuFrame5.place_forget()

# Save questions to the specified document
def saveQuestions(doc_num):
    global lines1, lines2, lines3, lines4, lines5, current_doc, last_doc
    current_doc = doc_num
    last_doc = doc_num  # Remember which document was just saved
    content = text_boxes[doc_num - 1].get("1.0", "end").strip()
    file_path = file_paths[doc_num - 1]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    lines1 = load_document_lines(1)
    lines2 = load_document_lines(2)
    lines3 = load_document_lines(3)
    lines4 = load_document_lines(4)
    lines5 = load_document_lines(5)
    getQ()
    fLoadQ()
    showQAHome()

# Show home page
def showHome():
    hide_all_frames()
    HomeP.place(x=0, y=100, relwidth=1, relheight=1)

# Show document selection page
def showQAHome():
    hide_all_frames()
    QAhome.place(x=0, y=100, relwidth=1, relheight=1)

# Show document editor
def showDoc(doc_num):
    global current_doc, last_doc
    last_doc = doc_num  # Remember which document was selected
    current_doc = doc_num
    hide_all_frames()
    frame = docuFrame1 if doc_num == 1 else docuFrame2 if doc_num == 2 else docuFrame3 if doc_num == 3 else docuFrame4 if doc_num == 4 else docuFrame5
    textbox = docuText1 if doc_num == 1 else docuText2 if doc_num == 2 else docuText3 if doc_num == 3 else docuText4 if doc_num == 4 else docuText5
    file_path = fileDoc1 if doc_num == 1 else fileDoc2 if doc_num == 2 else fileDoc3 if doc_num == 3 else fileDoc4 if doc_num == 4 else fileDoc5

    frame.place(x=0, y=100, relwidth=1, relheight=1)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    textbox.delete("1.0", "end")
    textbox.insert("1.0", content)

# Show quiz
def showQuiz():
    global lines1, lines2, lines3, lines4, lines5
    lines1 = load_document_lines(1)
    lines2 = load_document_lines(2)
    lines3 = load_document_lines(3)
    lines4 = load_document_lines(4)
    lines5 = load_document_lines(5)
    hide_all_frames()
    QA.place(x=0, y=100, relwidth=1, relheight=1)
    getQ()

# Show flashcards
def showfCard(doc_num=None):
    global current_doc, lines1, lines2, lines3, lines4, lines5, last_doc

    if doc_num is None:
        doc_num = last_doc  # fallback to last used document

    current_doc = doc_num
    last_doc = doc_num

    lines1 = load_document_lines(1)
    lines2 = load_document_lines(2)
    lines3 = load_document_lines(3)
    lines4 = load_document_lines(4)
    lines5 = load_document_lines(5)

    hide_all_frames()
    fGetQ()
    #FCfront.place(x=0, y=125, relwidth=1, relheight=1)

# Get random question
def getQ():
    active_lines = get_active_lines()
    if len(active_lines) < 2:
        result.configure(text=f"No questions in Document {current_doc}. Please add questions first.")
        return
    global num
    submitButton.configure(text="Submit", command=quest)
    num = random.randrange(0, len(active_lines) - 1, 2)
    loadQ()

# Get random flashcard question
def fGetQ():
    active_lines = get_active_lines()
    if len(active_lines) < 2:
        fQuestion.configure(text=f"No questions in Document {current_doc}. Please add questions first.")
        return
    global num
    num = random.randrange(0, len(active_lines) - 1, 2)
    fLoadQ()

# Load and display quiz question
def loadQ():
    global Ans, qText, attempts
    attempts = 0
    active_lines = get_active_lines()
    qText = active_lines[num].strip() + "?"
    Ans = active_lines[num + 1].strip().lower()
    Question.configure(text=qText)
    answerBox.delete("1.0", "end")
    result.configure(text="")

# Check quiz answer
def quest():
    global attempts
    userAns = answerBox.get("1.0", "end").strip().lower()
    if userAns == "":
        result.configure(text="Please type an answer")
        return
    elif userAns != Ans:
        attempts += 1
        if attempts == 1:
            result.configure(text="That's not correct. 2 attempts remaining.")
        elif attempts == 2:
            result.configure(text="That's not correct. 1 attempt remaining.")
        else:
            result.configure(text=f"\nIncorrect again.\nThe actual answer is: {Ans}")
            submitButton.configure(text="Next Question", command=getQ)
            return
        answerBox.delete("1.0", "end")
    else:
        result.configure(text="Correct, well done!")
        submitButton.configure(text="Next Question", command=getQ)

# Load flashcard question
def fLoadQ():
    global fText, Ans
    active_lines = get_active_lines()
    if len(active_lines) < 2:
        fQuestion.configure(text=f"No questions in Document {current_doc}. Please add questions first.")
        return
    FCback.place_forget()
    FCfront.place(x=0, y=125, relwidth=1, relheight=1)
    fText = active_lines[num].strip()
    Ans = active_lines[num + 1].strip().lower()
    fQuestion.configure(text=fText)
    flipButton.configure(text="Flip", command=fLoadBack)

# Load flashcard back
def fLoadBack():
    hide_all_frames()
    FCback.place(x=0, y=125, relwidth=1, relheight=1)
    fLoadA()

# Load flashcard answer
def fLoadA():
    bQuestion.configure(text=Ans)
    BflipButton.configure(text="Flip", command=fLoadQ)
    nextQ.configure(text="Next Question", command=fGetQ)



# Main Code #
showHome()  # Shows home page on launch

# Configuring all buttons to call their respective functions
quizButton.configure(command=showQuiz)
qListButton.configure(command=showQAHome)
fCardButton.configure(command=lambda: showfCard(last_doc))
saveButton1.configure(command=lambda: saveQuestions(1))
saveButton2.configure(command=lambda: saveQuestions(2))
saveButton3.configure(command=lambda: saveQuestions(3))
saveButton4.configure(command=lambda: saveQuestions(4))
saveButton5.configure(command=lambda: saveQuestions(5))
doc1Button.configure(command=lambda: showDoc(1))
doc2Button.configure(command=lambda: showDoc(2))
doc3Button.configure(command=lambda: showDoc(3))
doc4Button.configure(command=lambda: showDoc(4))
doc5Button.configure(command=lambda: showDoc(5))

root.mainloop()