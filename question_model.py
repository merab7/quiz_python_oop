class Model:
    def __init__(self, q_num, text, answer, result, score):
        self.q_num = q_num
        self.text = text
        self.answer = answer
        self.result = result
        self.score = score

    def display_result_text(self):
        if self.result == "true":
            self.score += 1
            print(f"You got it right!\nThe correct answer was:{self.answer}\nYour current score is:{self.score}/"
                  f"{self.q_num} ")
        else:
            print(f"That's wrong.\nThe correct answer was:{self.answer}\nYour current score is:{self.score}/"
                  f"{self.q_num} ")
