import xml.etree.cElementTree as ET
import os
import shutil
import Classificator.upload_neiro as neiro
import time
import serial
import Classificator.MyJson as MyJson


class Hand():
    __path_to_program = ""
    __data_action = []
    __recognizer = ''
    __serial = ''


    def __init__(self,port,speed):
        self.__path_to_program = os.getcwd()
        path_to_json = self.__path_to_program + "/DATA/JSON/"
        self.__data_action.clear()
        self.__data_action = self.__create_data(path_to_json)
        self.__recognizer = neiro.Recognizer(self.__path_to_program)
        self.__serial = serial.Serial(port,speed)

    def __create_data(self,path_to_json):
        files = os.listdir(path=path_to_json)

        data = []
        if(files == []):
            print("Добавьте данные")
            exit()

        for file in files:
            num_tem = int(file.replace(".json",""))
            data_action = MyJson.get_action(path_to_json, file)
            #data_action[0] = data_action[0]+1
            #data_action.insert(1,1)

            data.append([num_tem,data_action])
        print(data)
        return data


    def __recognize_action(self,input_text):
        action = self.__recognizer.recognize(input_text)
        if action==None:
            print("Не распознано")
            return False
        data = self.__find_action_data(action)
        if data == None:
            print("Что то пошло не так")
            return False
        print(data)
        data = bytearray(data)
        return data

    def send_action(self,send_data):
        self.__serial.write(send_data)


    def contol_hand(self,text):
        data = self.__recognize_action(text)
        if(data != False):
            self.send_action(data)
            return True
        else:
            return False


    def __find_action_data(self,num_action):
        for action in self.__data_action:
            if(action[0]==num_action):
                return action[1]
        return None


#0bit - count_action
#1bit - iterable_action
#3bit - num_act_rep
#4bit... - action

pres_text = [
    "Сжать",            #0
    "Разжать",          #1
    "Клавиатура",       #2
    "Ок",               #3
    "Пока",             #4
    "Круто",            #5
    "Коза",             #6
]


if __name__ == "__main__":
    hand_rec = Hand("COM14",9600)

    """
    Порядок:
        На выходе -
         Привет - 4
         Сжать -  0
    На тестах:
        коза - 6
        разжать - 1
    """


    while(1):
        print("Введите фразу")
        text = input()
        print("Начал обработку")
        time.sleep(3)
        #print(pres_text[int(text)])
        try:
            hand_rec.contol_hand(pres_text[int(text)])
        except:
            pass




