import json
import os



def create_json(Path_to_prog):
    num_tem = 1
    const = ["Сжать","Сжатие","Сожми","   Выполнить сжатие "]
    count_action = 2
    name = "Сжать"
    iterable_action = 0
    num_act_rep = 1
    del_action1 = 100
    del_action2 = 100
    action = [255,255,255,255,255]
    action2 = [250,250,250,250,250]
    #a = json.dumps([
    '''
    data = [
        {info:{"num_tem":num_tem},
        {"name":name}},
        {"const":const},
        {"count_action":count_action},
        {"iterable_action":iterable_action},
        {"time_action":time_action},
        {"del_action1":del_action},
        {"action1":action}
         ]
    '''

    data = {
        "info":
            {
                "num_tem": num_tem,
                "name": name
            },

        "const": const,

        "info_action":
            {
                "count_action": count_action,
                "iterable_action": iterable_action,
                "num_act_rep": num_act_rep,
            },

        "actions":
                [{
                    "num_action":1,
                    "del_action": del_action1,
                    "action": action
                },
                {
                    "num_action": 2,
                    "del_action": del_action2,
                    "action": action2
                }
                ]

        }



    with open(Path_to_prog+'/DATA/JSON/'+str(num_tem)+'.json', 'w', encoding='utf-8') as outfile:
        json.dump(data,outfile,ensure_ascii=False)

    num_tem = 2
    const = ["Разжать", "Разжатие", "Рожать", "Разожми","   Выполнить разжатие "]
    count_action = 2
    name = "Разжать"
    iterable_action = 0
    num_act_rep = 1
    del_action = 0
    action = [0, 0, 0, 0 , 0]
    action2 = [5, 5, 5, 5, 5]



    data = {
        "info":
            {
                "num_tem": num_tem,
                "name": name
            },

        "const": const,

        "info_action":
            {
                "count_action": count_action,
                "iterable_action": iterable_action,
                "num_act_rep": num_act_rep,
            },

        "actions":
            [{
                "num_action": 1,
                "del_action": del_action1,
                "action": action
            },
                {
                    "num_action": 2,
                    "del_action": del_action2,
                    "action": action2
                }
            ]

    }

    with open(Path_to_prog + '/DATA/JSON/' + str(num_tem) + '.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)


def read_json(Path_to_prog):
    files = os.listdir(path=Path_to_prog + "/DATA/JSON/")
    #print(files)
    for file in files:
        with open(Path_to_prog + '/DATA/JSON/'+file, 'r', encoding='utf-8') as file:
            data = json.load(file)#,ensure_ascii=False)
        print(data)
    #print(data["actions"][1]["action"])


def get_data(Path_to_prog):
    files = os.listdir(path=Path_to_prog + "/DATA/JSON/")
    out_data = []
    for file in files:
        with open(Path_to_prog + '/DATA/JSON/'+file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        num_tem = data['info']['num_tem']
        text_const = data['const']
        text_const.append(data['info']['name'])

        count_const = len(text_const)
        num_tem_list = ([num_tem]*count_const)
        out_data.append([num_tem_list,text_const])
    return [out_data,len(files)]


def get_action(path_to_json,file_action):
    out_data = []
    with open(path_to_json + file_action, 'r', encoding='utf-8') as file:
        data = json.load(file)
    count_action = data['info_action']['count_action']
    iterable_action = data['info_action']['iterable_action']
    num_action_rep = data['info_action']['num_act_rep']

    out_data.append(count_action)
    out_data.append(iterable_action)
    out_data.append(num_action_rep)

    list_action = data['actions']
    for number in range(count_action):
        num_action = number+1
        for action in list_action:
            if(action['num_action']==num_action):
                out_data.append(action['del_action'])
                for angle in action['action']:
                    out_data.append(angle)
        #for
        #if(data['actions']['num_action'] == number):
        #    out_data.append()
    out_data.insert(0, 1)
    out_data.insert(0, len(out_data))
    return out_data

if __name__ == "__main__":
    Path_to_dir = os.getcwd()
    Path_to_prog = Path_to_dir.replace("\Classificator", '')
    #print(Path_to_prog)
    create_json(Path_to_prog)
    #read_json(Path_to_prog)
    #data = get_data(Path_to_prog)
    #print(data)
    #data = get_action(Path_to_prog,"1.json")



