from checker import check_user_exists, access_rights
# не импортируется модуль choose_run_test !!!

def user_controller():
    '''Предполагается вызвать метод на старте запуска, запрвшивает имя,
    вызывает метод проверк в базе, права доступа, если имени нет - создает юзера'''
    date_welcom = welcom_func()
    username = date_welcom[0]
    is_admin = date_welcom[1]
    if check_user_exists(User(username, is_admin)):
        if access_rights(User(username, is_admin)):
            admin_handler(User(username, is_admin))
        else:
            user_handler(User(username, is_admin))
    else:
        create_user()


def test_controller(test: dict):
    pass

def result_controller():
    pass
