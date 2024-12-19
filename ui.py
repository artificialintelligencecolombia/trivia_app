from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.configure(bg=THEME_COLOR)
        self.window.title('Trivia App')
        
        self.score = 0
        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg='white', padx=20, pady=20, font=("Arial", 20, "bold"))
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, background='white')
        self.question = self.canvas.create_text(
            150, 125, 
            text='Are you ready?', 
            font=("Arial", 20, "italic"), 
            fill="black",
            width=200
            )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        
        self.correct_btn_img = PhotoImage(file='./images/true.png')
        self.wrong_btn_img = PhotoImage(file='./images/false.png')
        self.correct_btn = Button(image=self.correct_btn_img)
        self.incorrect_btn = Button(image=self.wrong_btn_img)
        self.correct_btn.grid(row=2, column=0, padx=20, pady=20)
        self.incorrect_btn.grid(row=2, column=1, padx=20, pady=20)
        
        self.window.mainloop()
        