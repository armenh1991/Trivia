from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.window.config(pady=20, padx=20, bg=THEME_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0)
        self.false_image = PhotoImage(file="images/false.png")
        self.true_image = PhotoImage(file="images/true.png")
        self.window.title("Quizzler")
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.button_true = Button(image=self.true_image, highlightthickness=0, command=self.true_answer)
        self.button_true.grid(row=2, column=0)
        self.button_false = Button(image=self.false_image, highlightthickness=0, command=self.wrong_answer)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"No more questions, "
                                        f"Your score is: {self.quiz.score}/"
                                        f"{self.quiz.question_number}")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.score_label.config()

    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



