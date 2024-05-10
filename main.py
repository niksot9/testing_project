import json
from set_classes import Test




test = {
    'subject': 'astronomy',
    'questions_count': 10,
    'timer': True,
    'scoring_system': 1,
    'level': 'beginner',
    'questions': ['q_1', 'q_2', 'q_3', 'q_4', 'q_5', 'q_6', 'q_7', 'q_8', 'q_9', 'q_10', ],
    'answer': [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'],
               ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'],
               ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd']],
    'correct': ['a', 'b', 'a', 'b', 'b', 'c', 'c', 'd', 'a', 'b']
}



if __name__ == '__main__':
    test_1 = Test(test)
    print(test_1.check_empty())
    test_id = '1'
    print(test_1.get_test(test_id))
    print(test_1.put_test())
    # test_2 = Test(t)
    # test_2.put_test()
