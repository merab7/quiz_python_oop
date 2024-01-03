from data import question_data as qd
from quiz_brain import Brain
from question_model import Model
from random import choice


def play():
    qu_num = 0
    len_of_data = len(qd)
    score = 0

    while True:
        qu_num += 1
        len_of_data -= 1

        question = choice(qd)
        text = question["text"]
        correct_answer = question["answer"].lower()

        user_input = input(f"Q.{qu_num} {text}(True/False): ").lower()

        if user_input not in ["false", "true"]:
            print("You have two options, True or False. Please check your input")
            continue
        else:
            brain = Brain(answer=correct_answer, user_input=user_input)

            model = Model(answer=correct_answer,
                          q_num=qu_num,
                          result=brain.check(),
                          text=text,
                          score=score)

            model.display_result_text()
            if brain.check() == "true":
                score += 1
            if len_of_data == 0:
                break


play()
