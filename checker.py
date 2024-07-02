from repository import FILE_NAME
from models import Question, Answer, User
import sqlite3

CONNECTION_REPOSITORY = sqlite3.connect(FILE_NAME)

def check_test(new_test: dict):
    '''Получаем данные по test и проверяем они в ПОЛНОМ объеме в БД,
    если нет то возвращаемся в create_test для повторного ввода данных'''
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


def check_user_exists(new_user: User):
    'Проверяем существует админ/пользователь в БД'
    query = '''
        SELECT u.username, u.admin FROM users u
        VALUES (?, ?);
    '''
    cursor = CONNECTION_REPOSITORY.execute(query, (new_user.name, new_user.is_admin))
    data = cursor.fetchall()
    if (new_user.name, new_user.is_admin) in data:
        return True
    else:
        return False


def access_rights(new_user: User):
    'Проверяем права доступа админ/пользователь'
    # должен быть хеш пароля, реализованно просто булево соответствие админу
    try:
        query = '''
                    SELECT u.username, u.admin FROM users u
                    VALUES (?, ?);
                        '''
        cursor = CONNECTION_REPOSITORY.execute(query, (new_user.name, new_user.is_admin))
        data = cursor.fetchall()
        if new_user.is_admin == '1':
            return True
        else:
            return False
    except:
        return f'Not exists'



# x = {'subject': 'Astronomy', 'scoring_system': 1, 'complexity_level': 'beginer', 'questions': ['Largest planet in the solar system?'], 'answers': [['Earth', 'Mercury', 'Jupiter', 'Venus']], 'correct_answers': ['Jupiter']}
# print(check_test(x))