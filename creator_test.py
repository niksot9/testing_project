class TestCreator:
    def __init__(self):
        self.new_test = {}


    def create_test(self):
        new_subject = input('Введите название предмета: ')
        self.new_test['subject'] = new_subject
        new_questions_count = input('Введите колличество вопросов: ')
        self.new_test['questions_count'] = new_questions_count
        new_timer = input('Таймер True/False: ')
        self.new_test['timer'] = new_timer
        new_scoring_system = input('Введите систему подсчета очков 1/2/3: ')
        self.new_test['scoring_system'] = new_scoring_system
        new_level = input('Введите уровень сложности beginner/medium/advanced: ')
        self.new_test['level'] = new_level
        for i in range(1, int(new_questions_count) + 1):
            new_questions = input(f'Введите вопрос {i}: ')
            if 'questions' in self.new_test:
                self.new_test['questions'].append(new_questions)
            else:
                self.new_test['questions'] = [new_questions]
        for i in range(1, int(new_questions_count) + 1):
            new_answers = [input(f'Введите ответ {j} на тест {i}: ') for j in range(1, 5)]
            if 'answers' in self.new_test:
                self.new_test['answers'].append(new_answers)
            else:
                self.new_test['answers'] = [new_answers]
        for i in range(1, int(new_questions_count) + 1):
            new_correct = input(f'Введите правильный ответ на вопрос {i}: ')
            if 'correct' in self.new_test:
                self.new_test['correct'].append(new_correct)
            else:
                self.new_test['correct'] = [new_correct]
        return self.new_test
