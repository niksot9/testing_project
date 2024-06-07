from repository import BaseRepository
class TestView:

    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def get_test(self):
        pass

    def get_test_by_subject(self, subject):
        pass

