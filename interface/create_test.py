def creator_test():
    '''Интерфейс по созданию теста, заполняем 'сырыми' данными словарь, передаем в контроллер на проверку'''
    new_test = {'subject': input('Add subject: '),
                'scoring_system': input('Add scoring system: 1/2/3 '),
                'complexity_level': input('Add complexity_level beginner/average/advanced: '),
                'questions': [],
                'answers': [],
                'correct_answer': []
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

        new_test['correct_answer'].append(input(f'Add correct answer for question {count_questions}: '))
        count_questions += 1

    return new_test



# TODO: реализовать исключения при неправильном вводе данных теста -> проверка в контроллере