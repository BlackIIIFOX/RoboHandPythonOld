from gensim.models import Word2Vec
import Classificator.Learn_neiro.lemmatization as lemmatization
import os
import numpy as np




def text_in_vec(text,model): #для работы с клиентом
       try:
        # грузим векторное пространство
        #model = Word2Vec.load('C:\Учеба\_vectors.model')
        #model = Word2Vec.load('C:\Учеба/all_vectors.model')
        #model.init_sims(replace=True)

        count_word = 0  # кол-во слов в предложении(для работы с массивами)
        count_sentence = 0  # кол-во предложений в тексте(для работы с массивами)
        normal_text = lemmatization.get_sents([text])
        print(normal_text)
        for sentence in normal_text:  # проходит по всем предложениям в нормализированном тексте
            for word in sentence:  # проходит по всем словам в текущем предожении
                try:  # пытается выполнить данные действия,иначе переходит на следующие слово
                    if (count_word == 0):  # если первое слово в предложении,то создается новый массив
                        vector_word = model[word]  # создается новый массив и ему присваевается вектор слова
                    else:  # если это уже не первое слово
                        vector_word = vector_word + model[word]  # массивы суммируются
                    count_word = count_word + 1  # если все успешно,то увеличивается счетчик слов
                except:  # если что то не получилось,то
                    continue  # переходит на следующие слово
            if (type(vector_word) == np.ndarray):  # если тип является нужным(массивом)
                vector_word = vector_word / count_word  # находится средний вектор предложения
                #print(vector_word)
                if (count_sentence == 0):  # если это первое предложение
                    input = vector_word  # создается массив и ему присвается средий вектор предложения
                else:  # если это уже не первое предложение
                    input = np.vstack((input, vector_word))  # объединение выходного массива и среднего вектора
                count_sentence = sentence = count_sentence + 1  # счетчик предложений увиличивается
            vector_word = None  # удаляется переменная слова(средний вектор предложения)
            count_word = 0  # обнуляется счетчик слов
        #print(input)
        return input
       except:
           return False


def create_out(num_tem,len):
    out=np.zeros((len),dtype=int)
    out[num_tem-1]=1
    return out


def for_train(model,data,tems,out_length):
    count_word = 0  # кол-во слов в предложении(для работы с массивами)
    count_sentence = 0  # кол-во предложений в тексте(для работы с массивами)
    output = []
    #vector_word=None
    #print(data)
    number_tem = 0
    for const in data:  #проходим по каждой конструкции в таблице конструкций
        #normal_text = lemmatization.get_sents(id_and_const[1]) #переводим конструкцию в нормальную форму
        out = create_out(tems[number_tem], out_length)
        number_tem = number_tem+1
        #print(data)
        #print(out)

        #print(normal_text)
        #for sentence in normal_text: #проход по

        for word in const:  # проходит по всем словам в текущем предожении
                    try:  # пытается выполнить данные действия,иначе переходит на следующие слово
                        if (count_word == 0):  # если первое слово в предложении,то создается новый массив
                            vector_word = model[word]  # создается новый массив и ему присваевается вектор слова
                        else:  # если это уже не первое слово
                            vector_word = vector_word + model[word]  # массивы суммируются
                        count_word = count_word + 1  # если все успешно,то увеличивается счетчик слов
                    except:  # если что то не получилось,то
                        continue  # переходит на следующие слово
        if (type(vector_word) == np.ndarray):  # если тип является нужным(массивом)
                    vector_word = vector_word / count_word  # находится средний вектор предложения
                    if (count_sentence == 0):  # если это первое предложение
                        input = vector_word  # создается массив и ему присвается средий вектор предложения
                        output = out
                    else:  # если это уже не первое предложение
                        input = np.vstack((input, vector_word))  # объединение выходного массива и среднего вектора
                        output = np.vstack((output, out))
                    count_sentence= count_sentence + 1  # счетчик предложений увиличивается
            #print(vector_word,' ',out,' ',count_sentence,' ',id_and_const[1])
        vector_word = None  # удаляется переменная слова(средний вектор предложения)
        count_word = 0  # обнуляется счетчик слов
    return [input,output]
