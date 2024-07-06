from models import Question, Answer, User
import sqlite3
from pathlib import Path

FILE_NAME = Path(__file__).parent / Path('./storage/storage.db')
CONNECTION_REPOSITORY = sqlite3.connect(FILE_NAME)

def check_test(new_test: dict):
    '''Получаем данные по test и проверяем они в ПОЛНОМ объеме в БД,
    если нет, то возвращаемся в create_test для повторного ввода данных'''
    query = '''
        SELECT q.question, a.test_answer, q.correct_answer FROM tests t 
        INNER JOIN test_question tq 
        ON t.id = tq.test_id 
        INNER JOIN questions q 
        ON q.id = tq.question_id
        INNER JOIN answers a on a.question_id = q.id
        WHERE t.subject = ? AND t.scoring_system = ? AND t.complexity_level = ?
    '''
    cursor = CONNECTION_REPOSITORY.execute(query, (new_test['subject'], new_test['scoring_system'], new_test['complexity_level']))
    data = cursor.fetchall()
    if data == []:
        return False


    data_in_table = [Question(data[0][0], None, data[0][2])]
    for row in data:
        new_question = Question(row[0])
        new_answer = Answer(row[1])
        if new_question not in data_in_table:
            new_question.correct_answer = row[2]
            new_question.answers.append(new_answer)
            data_in_table.append(new_question)
        else:
            data_in_table[-1].answers.append(new_answer)


    data_new = []
    for i in range(len(new_test['questions'])):
        new_question = Question(new_test['questions'][i], new_test['answers'][i], new_test['correct_answers'][i])
        data_new.append(new_question)


    if len(data_in_table) != len(data_new):
        return False
    if [elem.answers and elem.correct_answer and elem.question for elem in data_in_table] == [elem.answers and elem.correct_answer and elem.question for elem in data_new]:
        print(f'Test exists, please re-enter: ')
        return True
    else:
        return False


def check_user_exists(user_data: list):
    'Проверяем существует админ/пользователь в БД, True - существует, False - не существует'
    query = '''
        SELECT u.username, u.admin FROM users u
        WHERE u.username = ? AND u.admin = ?;
    '''
    cursor = CONNECTION_REPOSITORY.execute(query, (user_data[0], user_data[1]))
    data = cursor.fetchall()
    if (user_data[0], user_data[1]) in data:
        return True
    else:
        return False


def access_rights(user_data: list):
    'Проверяем права доступа админ/пользователь, True - админ, False - пользователь'
    # должен быть хеш пароля, реализованно просто булево соответствие админу
    try:
        query = '''
            SELECT u.username, u.admin FROM users u
            WHERE u.username = ? AND u.admin = ?;
        '''
        cursor = CONNECTION_REPOSITORY.execute(query, (user_data[0], user_data[1]))
        data = cursor.fetchall()
        if user_data[1] == 1 and user_data[1] in data[0]:
            return True
        else:
            return False
    except:
        return False


def check_result(result_data: tuple):
    'Проверяем тест, подсчитываем сумму баллов'
    counter =0
    for i in result_data[0]:
        if result_data[0][i] == result_data[1][i]:
            counter += 1
    return counter


# x = {'subject': 'Astronomy', 'scoring_system': 1, 'complexity_level': 'beginer', 'questions': ['Largest planet in the solar system?'], 'answers': [['Earth', 'Mercury', 'Jupiter', 'Venus']], 'correct_answers': ['Jupiter']}
# print(check_test(x))