import serial
import gensim
#ports=[]


def find_ports():
    found = False
    ports = []
    for i in range(64):
        try:
            #port = "/dev/ttyS%d" % i
            #print(port)
            port = "COM%d" % i
            ser = serial.Serial(port)
            ser.close()
            print("Найден последовательный порт: ", port)
            ports.append(port)
            found = True
        except serial.serialutil.SerialException:
            pass

    if not found:
        print("Последовательных портов не обнаружено")
        return None
    return ports



def test_hand(ser):
    mez = 255
    bez = 255
    sr = 255
    uk = 255
    bol = 255
    del_act = 5
    data = [ 2, 1, 0, 1,del_act,mez,bez,sr,uk,bol,100,0,0,0,0,0]
    data.insert(0,len(data))

    ser.write(bytearray(data))
    #ser.close()

if __name__ == "__main__":

    #ports = find_ports()
    #exit()
    #ser = serial.Serial(ports[0], 9600)
    ser = serial.Serial("COM14", 9600)
    test_hand(ser)
    ser.close()