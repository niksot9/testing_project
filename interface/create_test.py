from checker import check_test

def creator_test():
    '''Интерфейс по созданию теста, заполняем 'сырыми' данными словарь, передаем в контроллер на проверку'''
    new_test = {'subject': input('Add subject: ').capitalize(),
                'scoring_system': int(input('Add scoring system (1 or 2): ')),
                'complexity_level': input('Add complexity_level (beginner or advanced): ').lower(),
                'questions': [],
                'answers': [],
                'correct_answers': []
                }

    count_questions = 1
    while True:
        new_question = input(f'Add question {count_questions} '
                             f'(or type "done" to finish adding questions): ')
        if new_question.lower() == 'done':
            break
        new_test['questions'].append(new_question)

        count_answers = 1
        new_answers = []
        while True:
            new_answer = input(f'Add answer {count_answers} for question {count_questions} '
                               f'(or type "done" to finish adding answers): ')
            if new_answer.lower() == 'done':
                break
            new_answers.append(new_answer)
            count_answers += 1
        new_test['answers'].append(new_answers)

        new_test['correct_answers'].append(input(f'Add correct answer for question {count_questions}: '))
        count_questions += 1

    while check_test(new_test):
        return creator_test()

    return new_test



# TODO: реализовать исключения при неправильном вводе данных теста -> проверка в контроллере на сообветствие всех данных как