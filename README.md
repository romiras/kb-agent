# kb-agent

Knowledge-Base agent allows to query Q&A dataset interactively in natural language.

## Use cases

* interactive lookup on FAQ
* assistant for smooth onboarding experience for new team members.

## How it works

1. Collecting Q&A in format as described in `docs/QA-dataset-spec.md` and storing it in `datasets/dataset.md`.
2. Generating SQLite database from collection of Q&A in `datasets/dataset.md`.
3. Generating vector embeddings using [txtai](https://neuml.github.io/txtai/) .
4. Querying indexed Q&A pairs interactively.

## Install

```shell
pip install -r requirements.txt
```

## Run demo

```shell
# Generate SQLite database answers.db from dataset.md
python gen_db.py

# run demo in CLI mode
python cli.py
```

## License

GNU AFFERO GENERAL PUBLIC LICENSE
