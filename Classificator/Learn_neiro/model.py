from gensim.models import Word2Vec
import Classificator.Learn_neiro.lemmatization as lemmatization
import os
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
import Classificator.Learn_neiro.text_in_vec as text_in_vec




def neiro(Path_to_prog,data,count_tem):

        # data[0] - tems, data[1] - const, data[2] -w2v
        input_output = text_in_vec.for_train(data[2],data[1],data[0],count_tem)

        print('Выборка переведена в допустимый формат')

        model = Sequential()
        model.add(Dense(70, input_dim=100, activation='relu'))
        model.add(Dense(35, activation='relu'))
        model.add(Dense(count_tem, activation='sigmoid'))

        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        model.fit(input_output[0], input_output[1], epochs=200, batch_size=2,verbose=2)


        # Генерируем описание модели в формате json
        model_json = model.to_json()
        # Записываем модель в файл
        json_file = open(Path_to_prog+"/DATA/Neiro/mnist_model.json", "w")
        json_file.write(model_json)
        json_file.close()


        model.save_weights(Path_to_prog+"/DATA/Neiro/my_model_weights.h5")
        print('Нейросеть обучена')


