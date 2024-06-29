def welcom_func():
    welcom = input('Welcome to the program! \n')
    username = input('Enter username: ')
    is_admin = input('Enter is_admin: ')
    return (username, is_admin)

def user_handler():
    '''Интерфейс для юзера'''
    pass

def admin_handler():
    '''Интерфейс для админа'''
    pass

def choice_test():
    print('Select a subject from the list: ')
    subject_list = get_all_subject()
    choice = input('').capitalize()
    if choice in subject_list:
        print('Select a test from the list: ')
        test_list = get_all_test_id_subject(choice)
        choice = input('')
        if choice in test_list:
            return choice
        else:
            print('No test')
            return choice_test()
    else:
        print('No subject')
        return choice_test()

def runing_test():
    '''Запускаем тест, ответы фиксируем в списке result'''
    result = []
    return result