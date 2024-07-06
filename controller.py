from checker import check_user_exists, access_rights, check_result
from interface.main_interface import creator_test, create_user, continue_func, create_user_func
from interface.choose_run_test_handlers import welcom_func, user_handler, admin_handler, choice_test, runing_test
from repository import SqliteRepository


def user_controller():
    '''Предполагается вызвать метод на старте запуска, запрвшивает имя,
    вызывает метод проверк в базе, права доступа, если имени нет - создает юзера'''
    date_welcom = welcom_func()
    if check_user_exists(date_welcom):
        if access_rights(date_welcom):
            admin_handler(date_welcom)
        else:
            user_handler(date_welcom)
    else:
        if continue_func():
            if create_user_func():
                repository_object = SqliteRepository()
                repository_object.add_new_user(create_user())
            else:
                return user_controller()
        else:
            print('Bye!')


def create_test_controller():
    '''Создаем тест, проверяем есть ли такой в БД, если есть создаем заного, если нет - добавляем в БД'''
    new_test = creator_test()
    while check_test(new_test):
        new_test = creator_test()
    return new_test


def result_controller():
    '''Выбираем тест по ID, запускаем его, передаем ответы, подсчитываем очки, добавляем в БД'''
    test_id = choice_test()
    runing_test_data = runing_test(test_id)
    score = check_result(runing_test_data)
    return test_id, score

