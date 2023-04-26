from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
import os

os.environ['OPENAI_API_KEY'] = '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'


def make_query(query):
    basse_prompt = 'give me top 3 links for *query*'
    query = f"{basse_prompt} {query}"
    print(index.query_with_sources(query))


if __name__ == "__main__":
    loader = TextLoader('data/pairs_link_desc.csv')
    index = VectorstoreIndexCreator().from_loaders([loader])
    while True:
        question = input('Enter your query: ')
        if question == 'q':
            exit(0)
        make_query(question)
