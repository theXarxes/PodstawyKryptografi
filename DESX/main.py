from functools import reduce
import PySimpleGUI as sg
import random


Table1 = [
    [57, 49, 41, 33, 25, 17, 9],
    [1, 58, 50, 42, 34, 26, 18],
    [10, 2, 59, 51, 43, 35, 27],
    [19, 11, 3, 60, 52, 44, 36],
    [63, 55, 47, 39, 31, 23, 15],
    [7, 62, 54, 46, 38, 30, 22],
    [14, 6, 61, 53, 45, 37, 29],
    [21, 13, 5, 28, 20, 12, 4]
]

Table2 = [
    [14, 17, 11, 24, 1, 5],
    [3, 28, 15, 6, 21, 10],
    [23, 19, 12, 4, 26, 8],
    [16, 7, 27, 20, 13, 2],
    [41, 52, 31, 37, 47, 55],
    [30, 40, 51, 45, 33, 48],
    [44, 49, 39, 56, 34, 53],
    [46, 42, 50, 36, 29, 32]
]
DesKeyCreator = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

PermutationTable = [
    [58, 50, 42, 34, 26, 18, 10, 2],
    [60, 52, 44, 36, 28, 20, 12, 4],
    [62, 54, 46, 38, 30, 22, 14, 6],
    [64, 56, 48, 40, 32, 24, 16, 8],
    [57, 49, 41, 33, 25, 17, 9, 1],
    [59, 51, 43, 35, 27, 19, 11, 3],
    [61, 53, 45, 37, 29, 21, 13, 5],
    [63, 55, 47, 39, 31, 23, 15, 7]
]

PermeutationTableReverse = [
    [40, 8, 48, 16, 56, 24, 64, 32],
    [39, 7, 47, 15, 55, 23, 63, 31],
    [38, 6, 46, 14, 54, 22, 62, 30],
    [37, 5, 45, 13, 53, 21, 61, 29],
    [36, 4, 44, 12, 52, 20, 60, 28],
    [35, 3, 43, 11, 51, 19, 59, 27],
    [34, 2, 42, 10, 50, 18, 58, 26],
    [33, 1, 41, 9, 49, 17, 57, 25]
]

Something = [
    [32, 1, 2, 3, 4, 5],
    [4, 5, 6, 7, 8, 9],
    [8, 9, 10, 11, 12, 13],
    [12, 13, 14, 15, 16, 17],
    [16, 17, 18, 19, 20, 21],
    [20, 21, 22, 23, 24, 25],
    [24, 25, 26, 27, 28, 29],
    [28, 29, 30, 31, 32, 1]
]

P = [
    [16, 7, 20, 21],
    [29, 12, 28, 17],
    [1, 15, 23, 26],
    [5, 18, 31, 10],
    [2, 8, 24, 14],
    [32, 27, 3, 9],
    [19, 13, 30, 6],
    [22, 11, 4, 25]
]

S1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

S2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

S3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
]

S4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]

S5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
]

S6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
]

S7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
]

S8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]



def Klucz(zmienna):
    if zmienna != 0:
        key =zmienna
    else:
        sample_letters = 'abcdefABCDEF0123456789'
        key = ''.join((random.choice(sample_letters)for i in range(16)))
    return key

def Klucz1xor(zmienna):
    if zmienna != 0:
        key =zmienna
    else:
        sample_letters = 'abcdefABCDEF0123456789'
        key = ''.join((random.choice(sample_letters)for i in range(16)))
    return key


def Klucz2xor(zmienna):
    if zmienna != 0:
        key =zmienna
    else:
        sample_letters = 'abcdefABCDEF0123456789'
        key = ''.join((random.choice(sample_letters)for i in range(16)))
    return key


def Klucze(Key):
    DESKeytoBinary = ["{0:04b}".format(int(i, 16)) for i in Key]
    DesKeytoString = ''.join(DESKeytoBinary)
    DesKeytoListOfString = list(DesKeytoString)

    KeyPermutation = []
    for i in range(8):
        for j in range(7):
            KeyPermutation.append(DesKeytoListOfString[Table1[i][j] - 1])

    KeyPermutationString = ''.join(KeyPermutation)

    LeftKey = KeyPermutationString[:int(len(KeyPermutationString) / 2)]
    RightKey = KeyPermutationString[int(len(KeyPermutationString) / 2):]


    LeftKeyList = [LeftKey]
    RightKeyList = [RightKey]
    j = 0
    for i in range(len(DesKeyCreator)):
        j = j + DesKeyCreator[i]
        LeftKeyList.append(LeftKey[j:] + LeftKey[:j])
        RightKeyList.append(RightKey[j:] + RightKey[:j])


    DESKeyPermutation2 = []
    for i in range(1, len(LeftKeyList)):
        m = list(LeftKeyList[i] + RightKeyList[i])
        DesKeyForPermutation2 = []
        for i in range(8):
            for j in range(6):
                DesKeyForPermutation2.append(m[Table2[i][j] - 1])
        DESKeyPermutation2.append(''.join(DesKeyForPermutation2))
    return  DESKeyPermutation2

Table12 = {}

for i in ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8'):
    Table12[i] = locals()[i]



def XOR(Key, Message, MessageLength):
    KeyList = list(Key)
    MessageList = list(Message)
    XorList = list()
    for i in range(MessageLength):
        XorList.append(str(int(KeyList[i]) ^ int(MessageList[i])))
    XorListString = ''.join(XorList)
    return XorListString



def binaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while binary != 0:
        TMP = binary % 10
        decimal = decimal + TMP * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def decimalToBinary(n):
    TMP = bin(n).replace("0b", "")
    return TMP.zfill(4)


def encrypt(list1, Key1, Key2, Key3):
    DESXAllBlcoks = []
    for i in range(len(list1)):
        MSG_List = ["{0:04b}".format(int(j, 16)) for j in list1[i]]
        print(MSG_List)
        MSG = list(''.join(MSG_List))
        print(MSG)
        MSG_String = ''

        Key2List = ["{0:04b}".format(int(i, 16)) for i in Key2]
        Key2_String = ''.join(Key2List)
        Key2_Single_list = list(Key2_String)

        TMP12 = XOR(Key2_Single_list, MSG, len(MSG))
        MSG = list(TMP12)



        for x in range(8):
            for y in range(8):
                MSG_String += MSG[PermutationTable[x][y] - 1]

        MSG_LEFT = MSG_String[:int(len(MSG_String) / 2)]
        MSG_RIGHT = MSG_String[int(len(MSG_String) / 2):]

        for j in range(16):
            TMP_MSG_LEFT = MSG_RIGHT
            MSG_TMP1 = ''
            MSG_TMP1_List = list(MSG_RIGHT)
            for x in range(8):
                for y in range(6):
                    MSG_TMP1 = MSG_TMP1 + MSG_TMP1_List[Something[x][y] - 1]
            DESXor = XOR(Klucze(Key1)[j], MSG_TMP1, len(MSG_TMP1))
            DESXORTMP = [DESXor[x:x + 6] for x in range(0, len(DESXor), 6)]
            S_KEYS = ''
            for l in range(len(DESXORTMP)):
                S_KEYS += decimalToBinary(
                    Table12['S' + str(l + 1)][binaryToDecimal(int(DESXORTMP[l][0] + DESXORTMP[l][5]))][binaryToDecimal(int(DESXORTMP[l][1:5]))])

            S_KEYS_LIST = list(S_KEYS)
            S_KEYS = ''
            for x in range(8):
                for y in range(4):
                    S_KEYS += S_KEYS_LIST[P[x][y] - 1]


            MSG_RIGHT = XOR(MSG_LEFT, S_KEYS, len(S_KEYS))
            MSG_LEFT = TMP_MSG_LEFT
        MSG_LEFT, MSG_RIGHT = MSG_RIGHT, MSG_LEFT

        AlmostThere = MSG_LEFT + MSG_RIGHT
        AlmostThere_LIST = list(AlmostThere)

        AlmostAlmostThere = ''
        for x in range(8):
            for y in range(8):
                AlmostAlmostThere += AlmostThere_LIST[PermeutationTableReverse[x][y] - 1]
        Key3toBinary = ["{0:04b}".format(int(i, 16)) for i in Key3]
        Key3toBianryString = ''.join(Key3toBinary)
        Key3EveryStringList = list(Key3toBianryString)


        AlmostAlmostThere=list(AlmostAlmostThere)

        AlmostAlmostThere = XOR(Key3EveryStringList, AlmostAlmostThere, len(AlmostAlmostThere))

        FromSingleListToComplexList = [AlmostAlmostThere[i:i + 4] for i in range(0, len(AlmostAlmostThere), 4)]

        DESXToHEx = [hex(int(i, 2)).replace("0x", "") for i in FromSingleListToComplexList]
        DESXString = ''.join(DESXToHEx)
        DESXAllBlcoks.append(DESXString)
    return DESXAllBlcoks


def decrypt(cipherText, key, Key2, Key3):
    DESXStringAllBlcoks = []
    for i in range(len(cipherText)):

        MSG_List = ["{0:04b}".format(int(j, 16)) for j in cipherText[i]]
        MSG = list(''.join(MSG_List))
        MSG_String = ''

        Key3toBinary = ["{0:04b}".format(int(i, 16)) for i in Key3]
        Key3ToString = ''.join(Key3toBinary)
        Key3StringToList = list(Key3ToString)

        TMP15 = XOR(Key3StringToList, MSG, len(MSG))
        MSG = list(TMP15)

        for x in range(8):
            for y in range(8):
                MSG_String += MSG[PermutationTable[x][y] - 1]

        LeftMSG = MSG_String[:int(len(MSG_String) / 2)]
        RightMSG = MSG_String[int(len(MSG_String) / 2):]

        for j in range(15, -1, -1):
            Left_temp_msg = RightMSG
            RightMSG_TMP = ''
            LeftMSG_TMP = list(RightMSG)
            for x in range(8):
                for y in range(6):
                    RightMSG_TMP = RightMSG_TMP + LeftMSG_TMP[Something[x][y] - 1]

            DESXFirstXor = XOR(Klucze(key)[j], RightMSG_TMP, len(RightMSG_TMP))
            XorString = [DESXFirstXor[x:x + 6] for x in range(0, len(DESXFirstXor), 6)]

            S_Keys = ''
            for l in range(len(XorString)):
                S_Keys += decimalToBinary(
                    Table12['S' + str(l + 1)][binaryToDecimal(int(XorString[l][0] + XorString[l][5]))][binaryToDecimal(int(XorString[l][1:5]))])

            S_Keys_List = list(S_Keys)
            S_Key = ''
            for x in range(8):
                for y in range(4):
                    S_Key += S_Keys_List[P[x][y] - 1]

            RightMSG = XOR(LeftMSG, S_Key, len(S_Key))
            LeftMSG = Left_temp_msg
        LeftMSG, RightMSG = RightMSG, LeftMSG

        MSG = LeftMSG + RightMSG
        MSG_List = list(MSG)
        AlmostThere = ''
        for x in range(8):
            for y in range(8):
                AlmostThere += MSG_List[PermeutationTableReverse[x][y] - 1]
        Key2ToBinary = ["{0:04b}".format(int(i, 16)) for i in Key2]
        KeyString = ''.join(Key2ToBinary)
        KeyStringToList = list(KeyString)
        AlmostThere = list(AlmostThere)
        AlmostThere = XOR(KeyStringToList, AlmostThere, len(AlmostThere))
        DESXtoBinary = [AlmostThere[i:i + 4] for i in range(0, len(AlmostThere), 4)]
        DESXBinaryToHex = [hex(int(i, 2)).replace("0x", "") for i in DESXtoBinary]
        DESXStringBlock = ''.join(DESXBinaryToHex)
        DESXStringAllBlcoks.append(DESXStringBlock)
    return DESXStringAllBlcoks


def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0' + hv
        lst.append(hv)
    return reduce(lambda x, y: x + y, lst)

def listtostring(y):
    str = ""
    for x in y:
        str += x
    return str


def odkodowanie(Key1, Key2, Key3, Text):
    FillWithZeroAndCut = [Text[i:i + 16] for i in range(0, len(Text), 16)]
    if len(FillWithZeroAndCut[-1]) != 16:
        FillWithZeroAndCut[-1] += '0' * (16 - len(FillWithZeroAndCut[-1]))
    msg3 = decrypt(FillWithZeroAndCut, Key1, Key2, Key3)
    print(msg3)
    for x in range(len(msg3)):
        print(bytes.fromhex(listtostring(msg3[x])).decode('utf-8'), end='')
    sg.popup('Odkodowana wiadomość to :', bytes.fromhex(listtostring(msg3)).decode('utf-8'))

def cos(msg1):

    Key1 = Klucz(0)                        #klucz do desa
    Key2 = Klucz1xor(0)                    #klucz do 1 xora
    Key3 = Klucz2xor(0)                    #klucz do 2 xora

    answer = toHex(msg1)
    FillWihtZeroAndCut = [answer[i:i + 16] for i in range(0, len(answer), 16)]
    if len(FillWihtZeroAndCut[-1]) != 16:
        FillWihtZeroAndCut[-1] += '0' * (16 - len(FillWihtZeroAndCut[-1]))
    m = encrypt(FillWihtZeroAndCut, Key1, Key2, Key3)
    print("Zakodwnana wiadmośc to : ", listtostring(m))
    print("Klucz 1 : ", Key1)
    print("Klucz 2 : ", Key2)
    print("Klucz 3 : ", Key3)
    sg.popup('Zakodowana wiadomość to :', listtostring(m),
             "Klucz DES to :", Key1,
             "Klucz 1 Xor to :", Key2,
             "Klucz 2 Xor to :", Key3)


layout = [
    [sg.Text("Algorytm DESX")],
    [sg.Button("Podaj treść do zakodowania"), sg.InputText()],
    [sg.Text("Podaj klucz 1 :"), sg.InputText()],
    [sg.Text("Podaj klucz 2 :"), sg.InputText()],
    [sg.Text("Podaj klucz 3 :"), sg.InputText()],
    [sg.Button("Podaj treść do odkodowania"), sg.InputText()]


]

window = sg.Window("DESX", layout)


while True:
    event, values = window.read()
    if event == "Podaj treść do zakodowania":
        msg1 =values[0]
        cos(msg1)
    if event == "Podaj treść do odkodowania":
        Key1 = values[1]
        Key2 = values[2]
        Key3 = values[3]
        Message = values[4]
        odkodowanie(Key1, Key2, Key3, Message)
    if event == sg.WIN_CLOSED:
        break

window.close()

