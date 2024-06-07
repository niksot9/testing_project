import  sqlite3

connection = sqlite3.connect('../storage/storage.db')
cursor = connection.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject VARCHAR(50) NOT NULL,
    scoring_system VARCHAR(50),
    complexity_level VARCHAR(50) NOT NULL);
    ''')

connection.commit()
connection.close()