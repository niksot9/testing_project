import json

FILE_NAME = 'storage.json'

class Test:
    def __init__(self, test):
        self.test = test


    def check_empty(self):
        '''Проверяем не пустой ли json и если пустой, добовляем пустой dict'''
        if isinstance(self, Test):
            with open(FILE_NAME, 'r+', encoding='utf-8') as f:
                file_content = f.read().strip()
                if not file_content:
                    file_content = {}
                    json.dump(file_content, f)
                    return f'Файл пустой'
                else:
                    return f'Файл не пустой'


    def clear_json(self):
        '''Чистим json, оставляем пустой dict'''
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            file_content = {}
            json.dump(file_content, f)


    def get_test(self, key_dict):
        '''Берем из json тест по test_id'''
        self.key_dict = key_dict
        if isinstance(self, Test):
            try:
                with open(FILE_NAME, 'r', encoding='utf-8') as f:
                    file_content = json.load(f)
                    try:
                        return file_content[key_dict]
                    except KeyError:
                        return 'Такого теста нет'
            except json.JSONDecodeError:
                return f'Некоректная запись в файле json'



    def put_test(self):
        '''Добавляем в json тест, присвоив ему следующий порядковый номер test_id'''
        try:
            if isinstance(self, Test):
                with open(FILE_NAME, 'r', encoding='utf-8') as f:
                    file_content = json.load(f)
                    set_key = file_content.keys()
                with open(FILE_NAME, 'w', encoding='utf-8') as f:
                    if not set_key:
                        file_content[1] = self.test
                        json.dump(file_content, f, indent=2)
                    else:
                        set_key = list(file_content.keys())
                        key_json = int(set_key[-1]) + 1
                        file_content[key_json] = self.test
                        json.dump(file_content, f, indent=2)
        except json.JSONDecodeError:
            return f'Некоректная запись в файле json'



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




# TODO: написать механику по созданию теста

