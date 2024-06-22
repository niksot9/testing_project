from pathlib import Path
import sqlite3
from models import Test, Question, Answer

FILE_NAME = Path('./storage/storage.db').resolve()


class SqliteRepository:
    connection = None

    def __init__(self):
        self.connection = sqlite3.connect(FILE_NAME)

    def get_test_id(self, test_id: int):
        try:
            get_test_query = '''
                SELECT t.*, q.id, q.question, a.test_answer, a.id, q.correct_answer_id FROM tests t 
                INNER JOIN test_question tq 
                ON t.id = tq.test_id 
                INNER JOIN questions q 
                ON q.id = tq.question_id
                INNER JOIN answers a on a.question_id = q.id
                WHERE t.id = ?;
            '''
            cursor = self.connection.execute(get_test_query, (test_id,))
            data = cursor.fetchall()

            test = Test(
                subject = data[0][1],
                scoring_system = data[0][2],
                complexity_level = data[0][3],
                questions = [Question(data[0][5])]
            )
            for row in data:
                new_question = Question(row[5])
                new_answer = Answer(row[6])
                if new_question not in test.questions:
                    new_question.answers.append(new_answer)
                    test.questions.append(new_question)
                else:
                    test.questions[-1].answers.append(new_answer)
                if row[7] == row[8]:
                    test.questions[-1].correct_answer = new_answer
            return test
        except IndexError:
            return f'No tests on subject'

    def get_all_subject(self):
        query = """
        SELECT * FROM Tests;
        """
        cursor = self.connection.execute(query)
        data = cursor.fetchall()
        tests = []
        for row in data:
            tests.append(Test.from_array(row).subject)
        return f'Subjects: {tests}'

    def put_test(self, test: Test, question: Question, answer: Answer):
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



