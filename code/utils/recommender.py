import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
from utils import string_cleaner
import logging
from flask import Flask

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

EMBEDDING_FILE = 'trained/books.model'
BOOKS_CSV_FILE = 'data/books.csv'

model = Word2Vec.load(EMBEDDING_FILE)

df = pd.read_csv(BOOKS_CSV_FILE)
df['Desc'] = df['Desc'].astype(str)
df['cleaned'] = df['Desc'].apply(string_cleaner._removeNonAscii)
df['cleaned'] = df.cleaned.apply(func=string_cleaner.make_lower_case)
df['cleaned'] = df.cleaned.apply(func=string_cleaner.remove_stop_words)
df['cleaned'] = df.cleaned.apply(func=string_cleaner.remove_punctuation)
df['cleaned'] = df.cleaned.apply(func=string_cleaner.remove_html)

def vectors(x):
    
    # Creating a list for storing the vectors (description into vectors)
    global word_embeddings
    word_embeddings = []

    # Reading the each book description 
    for line in df['cleaned']:
        avgword2vec = None
        count = 0
        for word in line.split():
            if word in model.wv.vocab:
                count += 1
                if avgword2vec is None:
                    avgword2vec = model[word]
                else:
                    avgword2vec = avgword2vec + model[word]
                
        if avgword2vec is not None:
            avgword2vec = avgword2vec / count
        
            word_embeddings.append(avgword2vec)


def recommendations(title):
    
    # Calling the function vectors
    vectors(df)
    
    # Finding cosine similarity for the vectors
    cosine_similarities = cosine_similarity(word_embeddings, word_embeddings)

    # Taking the data from the books and store in new data frame called books
    books = df[['id', 'title', 'genre', 'author', 'image_link']]

    # Reverse mapping of the index
    indices = pd.Series(data=df.index, index=df['title']).drop_duplicates()

    idx = indices[title]
    sim_scores = list(enumerate(cosine_similarities[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    book_indices = [i[0] for i in sim_scores]
    scores = [i[1] for i in sim_scores]
    recommend = books.iloc[book_indices]    
    items = []
    scoreIndex = 0
    for index, row in recommend.iterrows():
        if title != row['title']:
            items.append({'id': row['id'], 'title': row['title'], 'genre': row['genre'], 'author': row['author'], 'image_link': row['image_link'], 'score': str(scores[scoreIndex])})
        scoreIndex = scoreIndex + 1

    return items