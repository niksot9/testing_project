import sqlite3
from models import Test

FILE_NAME = 'storage/storage.db'

class SqliteRepository:
    connection = None


    def __init__(self):
        self.connection = sqlite3.connect(FILE_NAME)

    def get_test_id(self, test_id: int):
        get_test_query = '''
            SELECT t.*, q.id, q.question, a.question_id, a.test_answer, q.correct_answer_id FROM tests t 
            INNER JOIN test_question tq 
            ON t.id = tq.test_id 
            INNER JOIN questions q 
            ON q.id = tq.question_id
            INNER JOIN answers a on a.question_id = q.id
            WHERE t.id = ?;
        '''
        cursor = self.connection.execute(get_test_query, (test_id,))
        data = cursor.fetchall()
        parsed = {
            'test_id': data[0][0],
            'subject': data[0][1],
            'scoring': data[0][2],
            'complexity': data[0][3],
            'questions': [],
            'answers': [],
            'correct': data[0][8]
        }
        for row in data:
            question = {
                'question_id': row[4],
                'question': row[5]
            }
            if question not in parsed['questions']:
                parsed['questions'].append(question)
            answer = {
                'question_id': row[6],
                'answer': row[7]
            }
            if answer not in parsed['answers']:
                parsed['answers'].append(answer)
        print(parsed)
        return data

    def get_test(self):
        query = """
        SELECT * FROM Tests;
        """
        cursor = self.connection.execute(query)
        data = cursor.fetchall()
        tests = []
        for row in data:
            tests.append(Test.from_array(row))
        return tests


    def put_test(self, test: Test):
        try:
            query = """
                    INSERT INTO tests (subject, scoring_system, complexity_level) 
                    VALUES (?, ?, ?)
                    RETURNING id;
                    """
            data_tuple = test
            cursor = self.connection.execute(query, data_tuple)
            self.connection.commit()
        except sqlite3.Error as error:
            print("Ошибка ввода данных", error)
        finally:
            self.connection.close()






class BaseRepository:
    pass


"""
import json
from models import Test

FILE_NAME = 'storage/storage.json'

def get_test(key_dict):
    '''Берем из json тест по test_id'''
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            file_content = json.load(f)
            try:
                return file_content[key_dict]
            except KeyError:
                print('Такого теста нет')
    except json.JSONDecodeError:
        print('Некоректная запись в файле json')


def put_test(test: dict):
    '''Добавляем в json тест, присвоив ему следующий порядковый номер test_id'''
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            file_content = json.load(f)
            set_key = file_content.keys()
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            if not set_key:
                file_content[1] = test
                json.dump(file_content, f, indent=2)
            else:
                set_key = list(file_content.keys())
                key_json = check_next_id(set_key)
                file_content[str(key_json)] = test
                json.dump(file_content, f, indent=2)
    except json.JSONDecodeError:
        print('Некоректная запись в файле json')


def check_next_id(id_lst: list):
    '''Проверяет ID и возвращает ближайший свободный по порядку'''
    if not id_lst:
        return 1
    num_1 = 0
    num_2 = 0
    for i in id_lst:
        num_1 = num_2
        num_2 = int(i)
        if num_2 - num_1 > 1:
            return num_1 + 1
    return int(id_lst[-1]) + 1


def del_test(test: Test):
    '''Берем из json тест и удаляем его'''
    if isinstance(test, Test):
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            file_content = json.load(f)
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            for key, value in file_content.items():
                if value == test:
                    del file_content[key]
                    json.dump(file_content, f, indent=2)


def check_empty():
    '''Проверяем не пустой ли json и если пустой, добовляем пустой dict'''
    with open(FILE_NAME, 'r+', encoding='utf-8') as f:
        file_content = f.read().strip()
        if not file_content:
            file_content = {}
            json.dump(file_content, f)
            print('Файл пустой')
        else:
            print('Файл не пустой')


def clear_json():
    '''Чистим json, оставляем пустой dict'''
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        file_content = {}
        json.dump(file_content, f)

"""

# TODO: покрыть тестами (как оттестировать ф-ии получения и записи в storage не используя основной storage, копировать) сетап?



