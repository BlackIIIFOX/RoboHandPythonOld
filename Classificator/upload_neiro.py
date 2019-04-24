import keras
from keras.models import Model
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import Classificator.Learn_neiro.text_in_vec as text_in_vec
import numpy as np
import Classificator.Learn_neiro.Module_MySQL as SQL
import os
from gensim.models import Word2Vec

#https://habrahabr.ru/post/321510/


'''
Path_to_dir = os.getcwd()
Path_to_prog = Path_to_dir.replace("\Classificator", '')

json_file = open(Path_to_prog+"\DATA/Neiro/mnist_model.json", "r")
loaded_model_json = json_file.read()
json_file.close()

loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights(Path_to_prog+"\DATA/Neiro/my_model_weights.h5")
loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#conn=SQL.connect()
#cursor = conn.cursor()


model = Word2Vec.load(Path_to_prog+"\DATA/Neiro/all_vectors.model")
model.init_sims(replace=True)
'''

class Recognizer():
    __w2v_model = ''
    __model_neiro = ''

    def __init__(self,Path_to_prog):
        json_file = open(Path_to_prog + "\DATA/Neiro/mnist_model.json", "r")
        loaded_model_json = json_file.read()
        json_file.close()
        self.__model_neiro = model_from_json(loaded_model_json)
        self.__model_neiro.load_weights(Path_to_prog + "\DATA/Neiro/my_model_weights.h5")
        self.__model_neiro.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.__w2v_model = Word2Vec.load(Path_to_prog + "\DATA/Neiro/all_vectors.model")
        self.__w2v_model.init_sims(replace=True)

    def num_tem(self,classes):
        count = 1
        for i in classes:
            if (round(i) == 1):
                return count
            count = count + 1
        return count


    def recognize(self,input):
        vectors = text_in_vec.text_in_vec(input, self.__w2v_model)
        try:
            if vectors == False:
                return
        except:
            pass
        try:
            vectors[0][0]
        except:
            vectors = np.array([vectors])

        classes = self.__model_neiro.predict(vectors)
        for _class in classes:
            num = self.num_tem(_class)
        return num









if __name__ == "__main__":
    Path_to_dir = os.getcwd()
    Path_to_prog = Path_to_dir.replace("\Classificator", '')
    rec = Recognizer(Path_to_prog)
    while(1):
        print("Введите текст")
        text = input()
        num=rec.recognize(text) #ТЕСТ
        print(num)
