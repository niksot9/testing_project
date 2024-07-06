#
# from controller import user_controller
#
# if __name__ == '__main__':
#     user_controller()

from interface.choose_run_test_handlers import user_handler

user_handler(['Person 1', 1])


# x = {'subject': 'Astronomy', 'scoring_system': 1, 'complexity_level': 'beginer', 'questions': ['Largest planet in the solar system?', 'Earth diameter?'], 'answers': [['12 742 km', '13 742 km', '14 742 km']], 'correct_answers': ['Jupiter', '12 742 km']}
# z = SqliteRepository()
# print(z.get_all_subject())



# u = User('Person 1', 1)
# print(check_user_exists(u))

# print(check_user_exists(create_admin()))


# print(access_rights(['Person 2', 0]))


# print(runing_test(1))



# repo = SqliteRepository()
# data = repo.get_all_subject()
# print(data)
# data = repo.get_test_id(1)
# print(data)
# test_new = SqliteRepository()
# # test_add = test_new.put_test(Test(3, 'Algebra', 1, 'beginer' ).test_output())
#
# test_conrtoller = TestView(repo)
