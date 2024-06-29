class Answer:
    test_answer: str

    def __init__(self, test_answer):
        self.test_answer = test_answer

    def __repr__(self):
        return self.test_answer


class Question:
    question: str
    answers: list
    correct_answer: str

    def __init__(self, question, answers=[], correct_answer=None):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

    def __eq__(self, other):
        return (isinstance(other, Question)
                and self.question == other.question)

    def __repr__(self):
        return (f'Question: {self.question}, Answers: {self.answers}, '
                f'Correct: {self.correct_answer}')

class Test:
    subject: str
    scoring_system: int
    complexity_level: str
    questions: list

    def __init__(self, subject, scoring_system, complexity_level, questions=None):
        self.subject = subject
        self.scoring_system = scoring_system
        self.complexity_level = complexity_level
        self.questions = questions

    @classmethod
    def from_array(cls, data: tuple or list, questions=None):
        subject = data[1]
        scoring_system = data[2]
        complexity_level = data[3]
        return cls(subject, scoring_system, complexity_level, questions)

    def __repr__(self):
        return (f'Subject: {self.subject}, Scoring: {self.scoring_system}, '
                f'Complexity: {self.complexity_level}, Questions: {self.questions}')


class User:
    def __init__(self, name, is_admin):
        self.name = name
        self.is_admin = is_admin

    def __repr__(self):
        return f'Name: {self.name}, User: {self.is_admin}'


class Result:
    def __init__(self):
        pass

    def get_result(self):
        pass

    def put_result(self):
        pass
