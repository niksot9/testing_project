class Test:
    id: int
    subject: str
    scoring_system: int
    complexity_level: str

    def __init__(self, id, subject, scoring_system, complexity_level):
        self.id = id
        self.subject = subject
        self.scoring_system = scoring_system
        self.complexity_level = complexity_level

    @classmethod
    def from_array(cls, data: tuple or list):
        id = data[0]
        subject = data[1]
        scoring_system = data[2]
        complexity_level = data[3]
        return  cls(id, subject, scoring_system, complexity_level)

    def __repr__(self):
        return self.subject


    def test_output(self):
        return (self.id, self.subject, self.scoring_system, self.complexity_level)



class User:
    def __init__(self, id, is_admin):
        self.id = id
        self.is_admin = is_admin


class Result:
    def __init__(self):
        pass

    def get_result(self):
        pass

    def put_result(self):
        pass
