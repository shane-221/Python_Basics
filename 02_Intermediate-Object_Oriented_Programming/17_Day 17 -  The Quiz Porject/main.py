from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
object_question_bank=[]

    # Todo 1 : Creation of a question bank in a list using the class:
for i in question_data:
    new_question = Question(i["question"], i["correct_answer"])
    object_question_bank.append(new_question)

    # Todo 2: Bring up one of those questions.
quiz = QuizBrain(object_question_bank)
quiz.next_question()


    # Todo 3: Keep the questions running as a loop until the list is completed
while quiz.still_has_questions():
    quiz.next_question()

    # Todo: The presenting of the final score
print(f"You've completed the Quiz. Your final score is{quiz.score}/{quiz.question_number}")


