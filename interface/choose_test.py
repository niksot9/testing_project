import json
from repository import FILE_NAME

def access_rights():
    'Проверяем право доступа админ/пользователь'
    pass

def user_handler():
    'Интерфейс для юзера'
    pass

def admin_handler():
    'Интерфейс для админа'
    pass

def choice_test():
    '''Интерфейс выбора теста по ключевым полям'''
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        file_content = json.load(f)
    for i, elem in enumerate(file_content):
        print(i, elem)

print(choice_test())
