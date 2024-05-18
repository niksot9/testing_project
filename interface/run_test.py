def runing_test(test):
    '''Запускаем тест, ответы фиксируем в списке result'''
    result = []
    print(f"Тест {test['subject']} начат, {test['timer']}")
    for i, elem in enumerate(test['questions']):
        print(f'Вопрос {elem}')
        print(f"Варианты ответов {test['answers'][i]}")
        answer = input(f"Введите ответ a/b/c/d: ")
        result.append(answer)
    return result
