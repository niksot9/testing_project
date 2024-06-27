from pathlib import Path
import sqlite3
from models import Test, Question, Answer

FILE_NAME = Path(__file__).parent / Path('./storage/storage.db')


class SqliteRepository:
    connection = None

    def __init__(self):
        self.connection = sqlite3.connect(FILE_NAME)

    def get_test_id(self, test_id: int):
        try:
            get_test_query = '''
                SELECT t.*, q.id, q.question, a.test_answer, q.correct_answer FROM tests t 
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
                    new_question.answers.append(new_answer)
                    test.questions = [new_question if x == new_question else x for x in test.questions]
                test.questions[-1].correct_answer = row[7]
            return test
        except IndexError:
            return f'No tests on subject'

    def get_all_subject(self):
        query = '''
        SELECT * FROM Tests;
        '''
        cursor = self.connection.execute(query)
        data = cursor.fetchall()
        tests = []
        for row in data:
            tests.append(Test.from_array(row).subject)
        return f'Subjects: {tests}'


    def add_new_answer(self, new_answers: dict, question_id: int):
        try:
            query = '''
                    INSERT INTO answers (test_answers, question_id)
                    VALUES (?, ?);
                    '''
            cursor = self.connection.cursor()
            cursor.execute('BEGIN')
            for i in range(len(new_answers)):
                cursor.execute(query, (new_answers[i], question_id))
                cursor.execute('COMMIT')
        except sqlite3.Error:
            print('Transaction error')
            cursor.execute('ROLLBACK')


    def add_new_question(self, new_questions: list, new_answers: list, correct_answers: list, test_id: int):
        try:
            query = '''
                    INSERT INTO questions (question, correct_answer_id)
                    VALUES (?, ?)
                    RETURNING id;
                    '''
            cursor = self.connection.cursor()
            cursor.execute('BEGIN')
            for i in range(len(new_questions)):
                cursor.execute(query, (new_questions[i], correct_answers[i]))
                question_id = cursor.fetchone()
                cursor.execute('COMMIT')
                self.add_new_answer(new_answers, question_id)
        except sqlite3.Error:
            print('Transaction error')
            cursor.execute('ROLLBACK')


    def add_new_test(self, new_test: dict):
        try:
            query = '''
                    INSERT INTO tests (subject, scoring_system, complexity_level)
                    VALUES (?, ?, ?)
                    RETURNING id;
                    '''
            cursor = self.connection.cursor()
            cursor.execute('BEGIN')
            cursor.execute(query, (new_test['subject'], new_test['scoring_system'], new_test['complexity_level']))
            test_id = cursor.fetchone()
            cursor.execute('COMMIT')
            self.add_new_question(new_test['questions'], new_test['answers'], new_test['correct_answers'], test_id[0])
        except sqlite3.Error:
            print('Transaction error')
            cursor.execute('ROLLBACK')
        finally:
            self.connection.close()


# t = SqliteRepository()
# x = {'subject': 'Geo', 'scoring_system': 1, 'complexity_level': 'beg', 'questions': ['q1', 'q2'], 'answers': [['a1', 'a2', 'a3'], ['a1']], 'correct_answers': ['a2', 'a1']}
# print(t.add_new_test(x))

t = SqliteRepository()
print(t.get_test_id(1))



# class BaseRepository:
#     pass





# TODO: покрыть тестами (как оттестировать ф-ии получения и записи в storage не используя основной storage, копировать) setup?