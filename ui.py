from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        #canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text((150, 125),
                            text="Some sort of text", fill=THEME_COLOR,
                            font=("ariel", 20, "italic"), width=275)

        #buttons
        check_img = PhotoImage(file="./images/true.png")
        self.btnCheck = Button(image=check_img, pady=40, command=self.true_pressed)
        self.btnCheck.grid(column=0, row=2)

        wrong_img = PhotoImage(file="./images/false.png")
        self.btnWrong = Button(image=wrong_img, pady=40, command=self.false_pressed)
        self.btnWrong.grid(column=1, row=2)

        #Score
        self.score = Label(self.window, text=f"Score 0")
        self.score.config(pady=20, padx=20, bg=THEME_COLOR, font=("italic", 20, "bold"), fg="white")
        self.score.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.btnCheck.config(state="disabled")
            self.btnWrong.config(state="disabled")

    def true_pressed(self):
         self.give_feedback(self.quiz.check_answer("true"))
    def false_pressed(self):
         self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

