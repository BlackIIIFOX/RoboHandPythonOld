import os
import Classificator.Learn_neiro.create_model as create_model
import Classificator.Learn_neiro.model as model
import Classificator.MyJson as MyJson

Path_to_dir = os.path.dirname(os.path.realpath(__file__))
Path_to_prog = Path_to_dir.replace("\Classificator\Learn_neiro", '')
def learn_neiro():

    try:
        data = MyJson.get_data(Path_to_prog)
        count_tem = data[1]
        print("Создание векторного пространства...")
        data = create_model.create(Path_to_prog, data[0])
        print("Создание векторного пространства завершено.")
        print("Обучение нейросети...")
        model.neiro(Path_to_prog, data, count_tem)
        print("\nОбучение завершено")
    #except:
    #    print("Обучение не удалось")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    learn_neiro()

