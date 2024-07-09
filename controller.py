from checker import check_user_exists, access_rights, check_result, check_test
from interface.main_interface import creator_test, create_user, create_admin, continue_func, create_user_func
from interface.choose_run_test_handlers import welcome_func, user_handler, admin_handler, choice_test, runing_test
from repository import SqliteRepository


def start_controller():
    '''Предполагается вызвать метод на старте запуска, запрашивает имя,
    вызывает метод проверки в базе, права доступа, если имени нет - создает юзера'''
    data_welcome = welcome_func()
    if check_user_exists(data_welcome):
        if access_rights(data_welcome):
            admin_controller(data_welcome, choice_data=admin_handler())
        else:
            user_controller(data_welcome, choice_data=user_handler())
            return user_handler()
    else:
        if continue_func():
            if create_user_func():
                repository_object = SqliteRepository()
                repository_object.add_new_user(create_user())
            else:
                return start_controller()
        else:
            print('Bye!')


def create_test_controller():
    '''Создаем тест, проверяем есть ли такой в БД, если есть создаем заного, если нет - добавляем в БД'''
    new_test = creator_test()
    while check_test(new_test):
        new_test = creator_test()
    return new_test


def result_controller():
    '''Выбираем тест по ID, запускаем его, передаем ответы, подсчитываем очки'''
    test_id = choice_test()
    runing_test_data = runing_test(test_id)
    score = check_result(runing_test_data)
    return test_id, score


def user_controller(data_welcome, choice_data: int):
    '''Основная логика пользовательского обработчика, в зависимости от номера команды, выполняет действия'''
    user_object = SqliteRepository()
    if choice_data == 1:
        start_test = result_controller()
        user_id = user_object.get_user_id(data_welcome[0])
        user_object.add_new_result(start_test[0], user_id, start_test[1])
        print('Test completed!')
    if choice_data == 2:
        user_id = user_object.get_user_id(data_welcome[0])
        print(user_object.get_result_user(user_id))
    if choice_data == 3:
        user_object.add_new_user(create_user())


def admin_controller(data_welcome, choice_data: int):
    '''Основная логика админского обработчика, в зависимости от номера команды, выполняет действия'''
    admin_object = SqliteRepository()
    if choice_data == 1:
        test_id = choice_test()
        print(admin_object.get_test_id(test_id))
    if choice_data == 2:
        admin_object.add_new_test(create_test_controller())
        print('Test added')
    if choice_data == 3:
        print(admin_object.get_all_user())
        user_id = admin_object.get_user_id(input('Enter username:'))
        print(admin_object.get_result_user(user_id))
    if choice_data == 4:
        print(admin_object.get_all_user())
    if choice_data == 5:
        admin_object.add_new_admin(create_admin())
    if choice_data == 6:
        admin_object.add_new_user(create_user())
