## Maana NLTK service

This is a template for creating a Maana Knowledge Service in Python. This requires python 3.6+

## Installation

To install the python packages required, run this:

```
pip install -r requirements.txt
```

then open python and run these commands

```
import nltk
nltk.download()
```

at the prompt, download 'all'

## Starting

python server.py

## Queries to try


Adds a sentence:
    ```
    curl -XPOST http://localhost:7357/graphql -H 'Content-Type: application/json' -d '{"query": "mutation M { addSentence: addEmployee(id: \"asdf\", text: \"bob is awesome\") { id } }"}'
    ```

Gets all sentences:
    ```
    curl -X POST -H "Content-Type: application/json" -d '{ "query": "{ allSentences { text } }" }' http://localhost:7357/graphql

This will also automatically parse a the first columne of a file added for text and add sentences using NLTK. Drop a text file into Maana with loader running and see what happens!