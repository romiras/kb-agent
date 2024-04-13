from os import path
from txtai.embeddings import Embeddings

EMBEDDINGS_DATA_DIR = "./embeddings_data"
MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Create an instance of Embeddings using a transformer model
def init_embeddings(conn):
    embeddings = Embeddings({"method": "transformers", "path": MODEL, "content": "sqlite"})
    if path.isdir(EMBEDDINGS_DATA_DIR):
        embeddings.load(EMBEDDINGS_DATA_DIR)
    else:
        index_answers(conn, embeddings)
        embeddings.save(EMBEDDINGS_DATA_DIR)

    return embeddings

# create embeddings index from Q&A pairs
def index_answers(conn, embeddings):
    # Create a cursor object
    cur = conn.cursor()

    # Execute the query to fetch all records from the 'answers' table
    cur.execute("SELECT * FROM answers")

    data = []
    while True:
        rows = cur.fetchmany(500)  # Fetch 500 rows at a time
        if not rows:
            break

        # Create a list of tuples where each tuple is a record in the 'answers' table
        data.extend([(row[0], row[1], None) for row in rows])

        # Add data to the embeddings index using upsert
        embeddings.upsert(data)

def questions_with_answers_dict(conn, answer_uids):
    # Create a cursor object
    cur = conn.cursor()

    # Execute the query to fetch all records from the 'answers' table
    answer_uids_list = ",".join(answer_uids)
    cur.execute(f"SELECT id, question, answer FROM answers WHERE id IN ({answer_uids_list})")
    rows = cur.fetchall()
    return {row[0]: (row[1], row[2]) for row in rows}

def search_answers(question, embeddings, conn):
    # Now you can perform a lookup (search) in the indexed table
    results = embeddings.search(question)

    answer_uids = [result['id'] for result in results]
    id_to_question = questions_with_answers_dict(conn, answer_uids)

    # 'results' is a list of tuples where each tuple is (id, score)
    # 'id' is the index of the record in 'data' that matches the 'question'
    # 'score' is the similarity score of the match
    for result in results:
        answer_uid = int(result['id'])
        score = result['score']
        record = id_to_question[answer_uid]
        question = record[0]
        answer = record[1]
        print(f"## {question} (Score: {round(score, 3)})\n\n{answer}\n")
