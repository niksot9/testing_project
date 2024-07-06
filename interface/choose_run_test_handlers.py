from repository import SqliteRepository
from controller import result_controller

def welcom_func():
    print('Welcome to the test-program!')
    username = input('Enter username: ')
    is_admin = input('Enter is_admin: ')
    return [username, is_admin]


def user_handler(user_data: list):
    '''Интерфейс для юзера'''
    while True:
        choice = input('Enter 1 - Choice test \n'
                       'Enter 2 - Show user result \n'
                       'Enter 3 - Create new user \n'
                       'Enter 4 - Exit \n')
        if choice == 1:
            start_test = result_controller()
            user_object = SqliteRepository
            user_id = user_object.get_user_id(user_data[0])
            user_object.add_new_result(start_test[0], user_id, start_test[1])



def admin_handler(admin_date: list):
    '''Интерфейс для админа'''
    pass


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
            return choice
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