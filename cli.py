import sqlite3
from embeddings_helper import init_embeddings, search_answers

if __name__ == "__main__":
    # Connect to the SQLite database
    conn = sqlite3.connect('answers.db')

    try:
        embeddings = init_embeddings(conn)

        while True:
            question = input('Your question: ')
            if len(question) == 0:
                break

            search_answers(question, embeddings, conn)

    finally:
        conn.close() # Close the connection
