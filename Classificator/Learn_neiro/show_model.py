from gensim.models import Word2Vec
import Classificator.Learn_neiro.lemmatization as lemmatization
import numpy
from sklearn.manifold import TSNE
import pandas as pd
import matplotlib.pyplot as plt

#Это для построения модели векторного простанства
def plot(Path_to_prog):

   model = Word2Vec.load(Path_to_prog+'/DATA/Neiro/all_vectors.model')
   model.init_sims(replace=True)
   vocab = list(model.wv.vocab)
   X = model[vocab]

   tsne = TSNE(n_components=2)
   X_tsne = tsne.fit_transform(X)

   df = pd.concat([pd.DataFrame(X_tsne),
                    pd.Series(vocab)],
                   axis=1)

   df.columns = ['x', 'y', 'word']
   print(df)

   fig = plt.figure()
   ax = fig.add_subplot(1, 1, 1)

   ax.scatter(df['x'], df['y'])


   for i, txt in enumerate(df['word']):
       ax.annotate(txt, (df['x'].iloc[i], df['y'].iloc[i]))

   plt.show()


import os
Path_to_dir = os.getcwd()
Path_to_prog = Path_to_dir.replace("\Classificator\Learn_neiro", '')
plot(Path_to_prog)