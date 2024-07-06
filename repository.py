from pathlib import Path
import sqlite3
from models import Test, Question, Answer, User, Result

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
                questions = [Question(data[0][5], None, data[0][7])]
            )
            for row in data:
                new_question = Question(row[5])
                new_answer = Answer(row[6])
                if new_question not in test.questions:
                    new_question.correct_answer = row[7]
                    new_question.answers.append(new_answer)
                    test.questions.append(new_question)
                else:
                    test.questions[-1].answers.append(row[6])
            return test
        except IndexError:
            return f'No tests on subject'


    def get_all_test_id_subject(self, subject: str):
        query = '''
            SELECT t.id FROM tests t
            WHERE t.subject = ?;
        '''
        cursor = self.connection.execute(query, (subject,))
        data = cursor.fetchall()
        id_subject = []
        for row in data:
            id_subject.append(row[0])
        return f'All id for {subject}: {id_subject}'


    def get_all_subject(self):
        query = '''
            SELECT * FROM tests;
        '''
        cursor = self.connection.execute(query)
        data = cursor.fetchall()
        tests = []
        for row in data:
            tests.append(Test.from_array(row).subject)
        return f'Subjects: {tests}'


    def get_all_user(self):
        query = '''
            SELECT u.username, u.admin FROM users u;
        '''
        cursor = self.connection.execute(query)
        data = cursor.fetchall()
        users = []
        for row in data:
            user = User(row[0], row[1])
            users.append([user.name, user.is_admin])
        return f'Users: {users}'


    def get_user_id(self, username):
        try:
            query = '''
                SELECT u.id FROM users u
                WHERE u.username = ?;
            '''
            cursor = self.connection.execute(query, (username,))
            data = cursor.fetchall()
            user = data[0]
            return f'UserID: {user}'
        except IndexError:
            print('User not exist')


    def get_result_user(self, user_id: int):
        query = '''
            SELECT r.test_id, r.score FROM results r
            INNER JOIN users u 
            ON r.user_id = u.id
            WHERE u.id = ?;
        '''
        cursor = self.connection.execute(query)
        data = cursor.fetchall()
        results = []
        for row in data:
            result = Result(row[0], user_id, row[1])
            result.append(result.test_id, result.score)
        return f'UserID {user_id} test results: {results}'


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

            for i in range(len(new_test['questions'])):
                query = '''
                    INSERT INTO questions (question, correct_answer)
                    VALUES (?, ?)
                    RETURNING id;
                '''
                cursor.execute(query, (new_test['questions'][i], new_test['correct_answers'][i]))
                question_id = cursor.fetchone()

                for j in range(len(new_test['answers'][i])):
                    query = '''
                        INSERT INTO answers (test_answer, question_id)
                        VALUES (?, ?);
                    '''
                    cursor.execute(query, (new_test['answers'][i][j], question_id[0]))

                query = '''
                    INSERT INTO test_question (test_id, question_id)
                    VALUES (?, ?);
                '''
                cursor.execute(query, (test_id[0], question_id[0]))
            cursor.execute('COMMIT')

        except sqlite3.Error:
            print('Transaction error')
            cursor.execute('ROLLBACK')
        except IndexError:
            print('Incomplete structure')
            cursor.execute('ROLLBACK')
        finally:
            self.connection.close()


    def add_new_admin(self, user_data: list):
        query = '''
            INSERT INTO users (username, admin)
            VALUES (?, ?);
        '''
        cursor = self.connection.cursor()
        cursor.execute(query, (user_data[0], user_data[1]))
        self.connection.commit()


    def add_new_user(self, user_data: list):
        query = '''
            INSERT INTO users (username, admin)
            VALUES (?, ?);
        '''
        cursor = self.connection.cursor()
        new_user_data = User(user_data[0], user_data[1])
        cursor.execute(query, (new_user_data.name, new_user_data.is_admin))
        self.connection.commit()


    def add_new_result(self, test_id, user_id, score):
        query = '''
            INSERT INTO results(test_id, user_id, score)
            VALUES (?, ?, ?);
        '''
        cursor = self.connection.cursor()
        new_result_data = Result(test_id, user_id, score)
        cursor.execute(query, (new_result_data.test_id, new_result_data.user_id, new_result_data.score))
        self.connection.commit()




# t = SqliteRepository()
# x = {'subject': 'Geo', 'scoring_system': 1, 'complexity_level': 'beg', 'questions': ['q1', 'q2'], 'answers': [['a1', 'a2', 'a3'], ['a1']], 'correct_answers': ['a2', 'a1']}
# print(t.add_new_test(x))

# t = SqliteRepository()
# print(t.get_test_id(1))







# TODO: покрыть тестами (как оттестировать ф-ии получения и записи в storage не используя основной storage, копировать) setup?