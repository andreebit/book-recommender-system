import pandas as pd
from gensim.models import Word2Vec
import string_cleaner

BOOKS_CSV_FILE = 'data/books.csv'
EMBEDDING_FILE = 'trained/GoogleNews-vectors-negative300.bin.gz'

df = pd.read_csv(BOOKS_CSV_FILE)
df['Desc'] = df['Desc'].astype(str)
df['cleaned'] = df['Desc'].apply(string_cleaner._removeNonAscii)
df['cleaned'] = df.cleaned.apply(func=string_cleaner.make_lower_case)
df['cleaned'] = df.cleaned.apply(func=string_cleaner.remove_stop_words)
df['cleaned'] = df.cleaned.apply(func=string_cleaner.remove_punctuation)
df['cleaned'] = df.cleaned.apply(func=string_cleaner.remove_html)


corpus = []
for words in df['cleaned']:
    corpus.append(words.split())


model = Word2Vec(vector_size=300, window=5, min_count=2, workers=-1)
model.build_vocab(corpus)
model.intersect_word2vec_format(EMBEDDING_FILE, lockf=1.0, binary=True)
model.train(corpus, total_examples=model.corpus_count, epochs=5)

model.save('trained/books.model')