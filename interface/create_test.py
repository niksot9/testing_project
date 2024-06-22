from repository import SqliteRepository
from models import Test, Question, Answer

class TestCreator:
    def __init__(self):
        self.test = Test()
        self.question = Question()
        self.answer = Answer()


    def creator_test(self):
        new_test = Test(
            subject=input('Add subject: '),
            scoring_system=input('Add scoring system: 1/2/3'),
            complexity_level=input('Add complexity_level beginner/average/advanced: '),
            questions=[Question(input('Add question 1: ')).question]
        )
        flag_questions = True
        count_questions = 2
        while flag_questions = True:
            new_question = Question(
                question=input(f'Add question {count_questions}: ')
                answers=[Answer(input('Add answer 1: ')).test_answer]
                flag_answers = True
                count_answers = 1
                while flag_answers = True:
                    new_answer = Answer(
                        answer=input(f'Add answers {count_answers}: '))
                    count_answers += 1
                    new_question.answers.append(new_answer)
                    answer_continue = input('Сontinue adding answers? y/n: ')
                    if answer_continue == 'y' or 'Y':
                        flag_answers = False
                correct_answer=input('Add correct answer: ')
            )
            count_questions += 1
            new_test.questions.append(new_question.answers)
            question_continue = input('Сontinue adding questions? y/n: ')
            if question_continue == 'y' or 'Y':
                flag_questions = False

        # put_test(self.test, self.question, self.answer)



test = TestCreator()
test.creator_test()


# TODO: реализовать исключения при неправильном вводе данных теста