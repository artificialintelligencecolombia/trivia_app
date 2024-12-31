from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain) -> None:
        self.quiz = quiz
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
            width=260
            )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        
        self.texto_res = Label(text="", font=("Arial", 15))
        self.texto_res.grid(row = 2, column = 0, columnspan = 2)
        self.texto_res.grid_forget()
        
        self.correct_btn_img = PhotoImage(file='./images/true.png')
        self.wrong_btn_img = PhotoImage(file='./images/false.png')
        self.correct_btn = Button(image=self.correct_btn_img, command=self.btn_verde)
        self.incorrect_btn = Button(image=self.wrong_btn_img, command=self.btn_rojo)
        self.correct_btn.grid(row=3, column=0, padx=20, pady=20)
        self.incorrect_btn.grid(row=3, column=1, padx=20, pady=20)
        
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self) -> None:
        self.canvas.config(background='white')
        self.texto_res.grid_forget()
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
        else:
            self.canvas.itemconfig(self.question, text='You have completed the quiz')
            self.correct_btn.config(state='disabled')
            self.incorrect_btn.config(state='disabled')
        
    def update_score(self) -> None:
        score = self.quiz.score
        self.score_label.config(text=f'Score: {score}')
        
    def btn_verde(self) -> None:
        answer = self.quiz.check_answer('true')
        self.feedback(answer)
        self.update_score()
        
    def btn_rojo(self) -> None:
        answer = self.quiz.check_answer('false')
        self.feedback(answer)
        self.update_score()
    
    def feedback(self, answr: bool) -> None:
        if answr == True:
            self.canvas.config(background='green')
            self.texto_res.config(text="Respuesta Correcta", fg="green")
            self.texto_res.grid(row = 2, column = 0, columnspan = 2)
        else:
            self.canvas.config(background='red')
            self.texto_res.config(text="Respuesta Incorrecta", fg="red")
            self.texto_res.grid(row = 2, column = 0, columnspan = 2)
        self.window.after(1000, self.get_next_question)
        
