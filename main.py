from repository import SqliteRepository
from checker import check_test

x = {'subject': 'Astronomy', 'scoring_system': 1, 'complexity_level': 'beginer', 'questions': ['Largest planet in the solar system?', 'Earth diameter?'], 'answers': [['Earth', 'Jupiter', 'Mercury', 'Venus'], ['12 742 km', '13 742 km', '14 742 km']], 'correct_answers': ['Jupiter', '12 742 km']}
print(check_test(x))



# repo = SqliteRepository()
# data = repo.get_all_subject()
# print(data)
# data = repo.get_test_id(1)
# print(data)
# test_new = SqliteRepository()
# # test_add = test_new.put_test(Test(3, 'Algebra', 1, 'beginer' ).test_output())
#
# test_conrtoller = TestView(repo)
