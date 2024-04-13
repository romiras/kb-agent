"""
Generate SQLite database answers.db from dataset.md
"""

import sqlite3

def parse_file(file_path):
    with open(file_path, 'r') as file:
        content = []
        mode = 'Q' # always starts from question
        for line in file:
            stripped_line = line.strip()
            if stripped_line.startswith('Q:'):
                content.append(stripped_line[3:])
            elif stripped_line.startswith('A:'):
                content.append(stripped_line[3:])
            elif stripped_line == '---':
                yield mode, ("\n".join(content)).strip()
                content = []
                mode = 'A'
            elif stripped_line == '-----':
                yield mode, "\n".join(content)
                content = []
                mode = 'Q'
            else:
                content.append(stripped_line)

def store_in_db(file_path, db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Create table if it doesn't exist
    cur.execute('''
        CREATE TABLE IF NOT EXISTS answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        )
    ''')

    # Parse the file and insert data into the database
    question = None
    for type, value in parse_file(file_path):
        if type == 'Q':
            question = value
        elif type == 'A' and question is not None:
            cur.execute('INSERT INTO answers (question, answer) VALUES (?, ?)', (question, value))
            question = None

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

file_path = './datasets/dataset.md'
db_path = 'answers.db'
store_in_db(file_path, db_path)
