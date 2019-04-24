import xml.etree.cElementTree as ET
import os
import shutil
import Classificator.upload_neiro as neiro
import time
import serial
import Classificator.MyJson as MyJson


'''
def getBatchNameFromXml(XML_path):
    try:
        tree = ET.parse(XML_path)
        #print(tree)
        root = tree.getroot()
        return root[0].text
    #except IOError as e:
    #    print(e)
    except:
        return
#path_to_program = "C:\Учеба/3 курс\Интелектуальный_интернет\Программы\python/robo_hand/"
path_to_program = os.getcwd()
data_directory = "/DATA"

path_to_XML = path_to_program+data_directory+"/XML/"


def reset_file():
    file=open("DATA/XML/file.xml","r")
    file_write=open("DATA/XML/file_utf.xml","w")
    for line in file:
        file_write.write(line.encode('utf-8').decode("cp1251"))
    file.close()
    file_write.close()


port = "COM4"

#values = bytearray([


#ser = serial.Serial(port,115200)
print("Начало работы...")
while True:
    file_list = os.listdir(path_to_XML)
    if(not file_list==0):
        for file in file_list:
            if(file=='file.xml'):
                time.sleep(0.1)
                reset_file()
                time.sleep(0.1)
                text=getBatchNameFromXml(path_to_XML + 'file_utf.xml')
                num_action=neiro.recognize(text)
                if(not num_action==None):
                    print(str(text) + " " + str(num_action))
                    #ser.write(bytes([num_action]))
                    #ser.close()
                else:
                    print(text+" не является допустимой конструкцией")
                os.remove(path_to_XML+'file.xml')
                os.remove(path_to_XML + 'file_utf.xml')
'''



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

if __name__ == "__main__":
    hand_rec = Hand("COM14",9600)

    while(1):
        print("Введите фразу")
        text = input()
        hand_rec.contol_hand(text)





