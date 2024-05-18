from models import Test
from repository import get_test, put_test, del_test, del_test, check_empty, clear_json
from interface.create_test import TestCreator


test = {
    'subject': 'astronomy',
    'questions_count': 10,
    'timer': True,
    'scoring_system': 1,
    'level': 'beginner',
    'questions': ['q_1', 'q_2', 'q_3', 'q_4', 'q_5', 'q_6', 'q_7', 'q_8', 'q_9', 'q_10', ],
    'answers': [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'],
               ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'],
               ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd']],
    'correct': ['a', 'b', 'a', 'b', 'b', 'c', 'c', 'd', 'a', 'b']
}



if __name__ == '__main__':
    check_empty()
    t1_new = TestCreator()
    t1_new.creator_test()

    # test_id = '1'
    # print(test_1.get_test(test_id))

    # test_2 = Test(t)
    # test_2.put_test()
