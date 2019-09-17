import Classificator.Learn_neiro.lemmatization as lemmatization
from gensim.models import Word2Vec, Phrases
import gensim.models
import os

def create(Path_to_prog,data):

        input_data = []
        input_tem = []
        for list in data:
            input_tem.extend(list[0])
            input_data.extend(list[1])

        try:
           #sents = lemmatization.get_sents(text_const) #разбивает строку и приводит каждое слово строки к нормальной форме
           sents = lemmatization.get_sents(input_data)
           #print(sents)
        except:
           print('Лемантизация невозможная')
           exit()
        print('Этап лемантизации пройден')

        try:
           bigram_transformed = Phrases(sents)
           w2v= Word2Vec(bigram_transformed[sents],window=5,min_count=1,size=100,workers=4)  #cbow_mean=2
           w2v.init_sims(replace=True)
           w2v.save(Path_to_prog+'/DATA/Neiro/all_vectors.model')
        except:
           print('Создание модели невозможно')
           exit()

        print('Создание модели w2v проведено')

        return [input_tem,sents,w2v]








