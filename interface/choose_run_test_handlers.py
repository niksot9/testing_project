from repository import SqliteRepository


def welcome_func():
    print('Welcome to the test-program!')
    username = input('Enter username: ')
    is_admin = input('Enter is_admin: ')
    return [username, is_admin]


def user_handler():
    try:
        '''Интерфейс для юзера'''
        choice_list = [1, 2, 3, 4]
        choice = input('Enter 1 - Choice and run test \n'
                       'Enter 2 - Show user result \n'
                       'Enter 3 - Create new user \n'
                       'Enter 4 - Exit \n... ')
        if int(choice) in choice_list:
            return int(choice)
        else:
            print('Enter the number according to the list of options')
            return user_handler()
    except ValueError:
        print('Enter the number according to the list of options')
        return user_handler()


def admin_handler():
    '''Интерфейс для админа'''
    try:
        choice = input('Enter 1 - Choice test \n'
                       'Enter 2 - Add test \n'
                       'Enter 3 - Show user result \n'
                       'Enter 4 - Show all users \n'
                       'Enter 5 - Create new admin \n'
                       'Enter 6 - Create new user \n'
                       'Enter 7 - Exit \n... ')
        choice_list = [1, 2, 3, 4, 5, 6, 7]
        if int(choice) in choice_list:
            return int(choice)
        else:
            print('Enter the number according to the list of options')
            return admin_handler()
    except ValueError:
        print('Enter the number according to the list of options')
        return admin_handler()


def choice_test():
    subject_object = SqliteRepository()
    subjects_list = subject_object.get_all_subject()
    print(subjects_list)
    choice = input('Select a subject from the list: ').capitalize()
    if choice in subjects_list:
        tests_list = subject_object.get_all_test_id_subject(choice)
        print(tests_list)
        choice = input('Select a test from the list: ')
        if choice in tests_list:
            return int(choice)
        else:
            print('No test')
            return choice_test()
    else:
        print('No subject')
        return choice_test()


def runing_test(test_id: int):
    '''Запускаем тест, ответы фиксируем в списке result, правильные в correct'''
    test = SqliteRepository()
    run_test = test.get_test_id(test_id)
    print(f'{run_test.subject} test started!')
    result = []
    correct = []
    for question in run_test.questions:
        correct.append(question.correct_answer)
        print(question.question)
        for answer in question.answers:
            print(answer)
        result.append(input(f'Input answer: ').capitalize())
    return correct, result, test_id
