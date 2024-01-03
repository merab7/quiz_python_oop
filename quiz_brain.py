class Brain:
    def __init__(self, user_input, answer):
        self.user_input = user_input
        self.answer = answer

    def check(self):

        if self.user_input == self.answer:
            return "true"

        else:
            return "false"
