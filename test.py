from repository import SqliteRepository
from controller import TestView
from models import Test

repo = SqliteRepository()
data = repo.get_test()
print(data)
data = repo.get_test_id(1)
print(data)
test_new = SqliteRepository()
# test_add = test_new.put_test(Test(3, 'Algebra', 1, 'beginer' ).test_output())


test_conrtoller = TestView(repo)

