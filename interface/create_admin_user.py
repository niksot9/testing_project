from models import User
from checker import CONNECTION_REPOSITORY
from repository import FILE_NAME

def create_admin():
    username = input('Add username: ').capitalize()
    is_admin = '1'
    new_admin = User(username, is_admin)
        query = '''
            INSERT INTO users (username, admin)
            VALUES (?, ?);
        '''
    cursor = CONNECTION_REPOSITORY.cursor()
    cursor.execute(query, (new_admin.name, new_admin.is_admin))

def create_user():
    username = input('Add username: ').capitalize()
    is_admin = '0'
    new_admin = User(username, is_admin)
    query = '''
        INSERT INTO users (username, admin)
        VALUES (?, ?);
    '''
    cursor = CONNECTION_REPOSITORY.cursor()
    cursor.execute(query, (new_admin.name, new_admin.is_admin))