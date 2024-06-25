from repository import FILE_NAME
import sqlite3

CONNECTION_REPOSITORY = sqlite3.connect(FILE_NAME)

def check_test(new_test: dict):
    '''Получаем данные subject, scoring_system, complexity_level и проверяем есть ли они в БД,
    если нет то возвращаемся в create_test для повторного ввода данных таблицы tests'''
    query = ''' 
        SELECT subject, scoring_system, complexity_level FROM Tests 
        WHERE subject = ? AND scoring_system = ? AND complexity_level = ?
    '''
    cursor = CONNECTION_REPOSITORY.execute(query, (new_test['subject'], new_test['scoring_system'], new_test['complexity_level']))
    data = cursor.fetchall()

    if data:
        print(f'Test data {data[0][0]}, {data[0][1]}, {data[0][2]} exists, please re-enter: ')
        return True
    else:
        return False