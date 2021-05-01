from functools import reduce
import random
from math import ceil

M=78661
N=92797
Private_Key=[random.randint(150, 400)]
Public_Key=[]
MSG_final = []
decrypt_binary_list = []
def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0' + hv
        lst.append(hv)
    return reduce(lambda x, y: x + y, lst)


def szukanie(partlydecrypt):
    list=[]
    for x in range(8):
        for y in range(7):
            for z in range(6):
                for c in range(5):
                    for v in range(4):
                        for b in range(3):
                            for p in range(2):
                                for i in range(1):
                                    if (Private_Key[x] == partlydecrypt):
                                        list.append(x)
                                        tmp111 = 0
                                        for h in list:
                                            if list.count(h) <= 1:
                                                tmp111 += 1
                                        if (tmp111 == 1):
                                            list.clear()
                                            for ax in range(8):
                                                if ax != x:
                                                    list.append(10)
                                                else:
                                                    list.append(x)
                                            return list
                                        else:
                                            list.clear()
                                    if ( Private_Key[x] + Private_Key[y] == partlydecrypt):
                                        list.append(x)
                                        list.append(y)
                                        tmp111 = 0
                                        for h in list:
                                            if list.count(h) <= 1:
                                                tmp111 += 1
                                        if (tmp111 == 2):
                                            list.clear()
                                            for ax in range(8):
                                                if ax != x and ax != y:
                                                    list.append(10)
                                                elif ax==x:
                                                    list.append(x)
                                                elif ax==y:
                                                    list.append(y)
                                            return list
                                        else:
                                            list.clear()

                                    if (Private_Key[x] + Private_Key[y] +Private_Key[z] == partlydecrypt):
                                        list.append(x)
                                        list.append(y)
                                        list.append(z)
                                        tmp111 = 0
                                        for h in list:
                                            if list.count(h) <= 1:
                                                tmp111 += 1
                                        if (tmp111 == 3):
                                            list.clear()
                                            for ax in range(8):
                                                if ax != x and ax != y and ax!=z:
                                                    list.append(10)
                                                elif ax == x:
                                                    list.append(x)
                                                elif ax == y:
                                                    list.append(y)
                                                elif ax ==z:
                                                     list.append(z)
                                            return list
                                        else:
                                            list.clear()
                                    if (Private_Key[x] + Private_Key[y] + Private_Key[z] + Private_Key[c] == partlydecrypt):
                                        list.append(x)
                                        list.append(y)
                                        list.append(z)
                                        list.append(c)
                                        tmp111 = 0
                                        for h in list:
                                            if list.count(h) <= 1:
                                                tmp111 += 1
                                        if (tmp111 == 4):
                                            list.clear()
                                            for ax in range(8):
                                                if ax != x and ax != y and ax !=z and ax!=c:
                                                    list.append(10)
                                                elif ax == x:
                                                    list.append(x)
                                                elif ax == y:
                                                    list.append(y)
                                                elif ax == z:
                                                    list.append(z)
                                                elif ax == c:
                                                    list.append(c)
                                            return list
                                        else:
                                            list.clear()
                                    if (Private_Key[x] + Private_Key[y] + Private_Key[z] + Private_Key[c] + Private_Key[v] == partlydecrypt):
                                        list.append(x)
                                        list.append(y)
                                        list.append(z)
                                        list.append(c)
                                        list.append(v)
                                        tmp111 = 0
                                        for h in list:
                                            if list.count(h) <= 1:
                                                tmp111 += 1
                                        if (tmp111 == 5):
                                            list.clear()
                                            for ax in range(8):
                                                if ax != x and ax != y and ax != z and ax != c and ax!=v:
                                                    list.append(10)
                                                elif ax == x:
                                                    list.append(x)
                                                elif ax == y:
                                                    list.append(y)
                                                elif ax == z:
                                                    list.append(z)
                                                elif ax == c:
                                                    list.append(c)
                                                elif ax == v:
                                                    list.append(v)
                                            return list
                                        else:
                                            list.clear()
                                    if (Private_Key[x] + Private_Key[y] + Private_Key[z] + Private_Key[c] + Private_Key[v] + Private_Key[b] == partlydecrypt):
                                        list.append(x)
                                        list.append(y)
                                        list.append(z)
                                        list.append(c)
                                        list.append(v)
                                        list.append(b)
                                        tmp111=0
                                        for h in list:
                                            if list.count(h)<=1:
                                                tmp111 += 1
                                        if(tmp111==6):
                                            list.clear()
                                            for ax in range(8):
                                                if ax != x and ax != y and ax != z and ax != c and ax != v and ax !=b:
                                                    list.append(10)
                                                elif ax == x:
                                                    list.append(x)
                                                elif ax == y:
                                                    list.append(y)
                                                elif ax == z:
                                                    list.append(z)
                                                elif ax == c:
                                                    list.append(c)
                                                elif ax == v:
                                                    list.append(v)
                                                elif ax == b:
                                                    list.append(b)
                                            return list
                                        else:
                                            list.clear()
                                    if (Private_Key[x] + Private_Key[y] + Private_Key[z] + Private_Key[c] + Private_Key[v] + Private_Key[b] + Private_Key[p] == partlydecrypt):
                                        list.append(x)
                                        list.append(y)
                                        list.append(z)
                                        list.append(c)
                                        list.append(v)
                                        list.append(b)
                                        list.append(p)
                                        tmp111=0
                                        for h in list:
                                            if list.count(h)<=1:
                                                tmp111 += 1
                                        if(tmp111==7):
                                            list.clear()
                                            for ax in range(8):
                                                if ax != x and ax != y and ax != z and ax != c and ax != v and ax !=b and ax!=p:
                                                    list.append(10)
                                                elif ax == x:
                                                    list.append(x)
                                                elif ax == y:
                                                    list.append(y)
                                                elif ax == z:
                                                    list.append(z)
                                                elif ax == c:
                                                    list.append(c)
                                                elif ax == v:
                                                    list.append(v)
                                                elif ax == b:
                                                    list.append(b)
                                                elif ax == p:
                                                    list.append(p)
                                            return list
                                        else:
                                            list.clear()
                                    if (Private_Key[x] + Private_Key[y] + Private_Key[z] + Private_Key[c] + Private_Key[v] + Private_Key[b] + Private_Key[p]+Private_Key[i] == partlydecrypt):
                                        list.append(x)
                                        list.append(y)
                                        list.append(z)
                                        list.append(c)
                                        list.append(v)
                                        list.append(b)
                                        list.append(p)
                                        list.append(i)
                                        tmp111 = 0
                                        for h in list:
                                            if list.count(h) <= 1:
                                                tmp111 += 1
                                        if (tmp111 == 8):
                                            list.clear()
                                            for ax in range(8):
                                                if ax != x and ax != y and ax != z and ax != c and ax != v and ax != b and ax != p and ax!=i:
                                                    list.append(10)
                                                elif ax == x:
                                                    list.append(x)
                                                elif ax == y:
                                                    list.append(y)
                                                elif ax == z:
                                                    list.append(z)
                                                elif ax == c:
                                                    list.append(c)
                                                elif ax == v:
                                                    list.append(v)
                                                elif ax == b:
                                                    list.append(b)
                                                elif ax == p:
                                                    list.append(p)
                                                elif ax == i:
                                                    list.append(i)
                                            return list
                                        else:
                                            list.clear()


def generatePrivate_key():
    SUM=0
    for x in range(7):
        for y in Private_Key:
           SUM+=y
        TMP=SUM+random.randint(300, 1000)
        Private_Key.append(TMP)
        SUM=0

def generateM2():
    SUM = 0
    for y in Private_Key:
        SUM += y
    return SUM+random.randint(30000, 300000000000000000)

def generateN2():
    tmp1=M/2
    tmp2=M-1
    TMP1000=random.randint(ceil(tmp1), tmp2)
    while nwd(TMP1000, M)!=1:
        TMP1000 = random.randint(ceil(tmp1), tmp2)
    return TMP1000
def generateM():
    SUM = 0
    for y in Private_Key:
        SUM += y
    return SUM+random.randint(3000000, 10000000)

def generateN():
    tmp1=M/2
    tmp2=M-1
    TMP1000=random.randint(ceil(tmp1), tmp2)
    while nwd(TMP1000, M)!=1:
        TMP1000 = random.randint(ceil(tmp1), tmp2)
    return TMP1000

def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    else:
        return a


def generatePublic_key():
    for x in Private_Key:
        Public_Key.append((x * N) % M)


def encrypt(MSG):
    tmp = 0
    Tmp = []
    iteratorklucza = 0
    cos = 0
    for x in MSG:
        if tmp < 8:
            Tmp.append(x)
            if tmp == 7:
                for y in Tmp:
                    tmp2 = int(y)
                    tmp3 = Public_Key[iteratorklucza]
                    cos += tmp2 * tmp3
                    iteratorklucza += 1
                tmp = -1
                iteratorklucza = 0
                MSG_final.append(cos)
                cos = 0
                Tmp.clear()
        tmp += 1

def decrypt():
    ndo1 = 0
    tmp200 = []
    while (N * ndo1) % M != 1:
        ndo1 +=1
    for x in MSG_final:
        partlydecrypt = (x * ndo1) % M
        tmp200.append(szukanie(partlydecrypt))


    for x in tmp200:
        for y in x:
            if y == 10:
                decrypt_binary_list.append('0')
            else:
                decrypt_binary_list.append('1')

def listtostring(y):
    str = ""
    for x in y:
        str += x
    return str







WarunekAplikacji=10

while WarunekAplikacji!='0':
    print("Witaj użytkowniku")
    print("wpisz 0 - Zamknięcie programu")
    print("wpisz 1 - enkrypcja")
    print("wpisz 2 - dekrypcja")
    WarunekAplikacji=input()
    print(WarunekAplikacji)
    if WarunekAplikacji=='1':
        text=input("Podaj tekst do zaszyfrowania : ")
        text_hex = []
        text_hex.append(toHex(text))
        MSG_List = ["{0:04b}".format(int(j, 16)) for j in text_hex[0]]
        MSG = list(''.join(MSG_List))
        generatePrivate_key()
        M = generateM2()
        N = generateN2()
        generatePublic_key()
        encrypt(MSG)
        # print("N to : ", N)
        # print("M to : ", M)
        print("Klucz prywatny to : ", Private_Key)
        print("zaszyfrowana wiadmość to : ", MSG_final)
        # tmp0000=0
        # for x in Private_Key:
        #     tmp0000+=x.bit_length()
        # print(tmp0000)


    if WarunekAplikacji=='2':
        Private_Key.clear()
        Public_Key.clear()
        MSG_final.clear()
        tmp09="100"
        # N=int(input("Podaj N : "))
        # M=int(input("Podaj M : "))
        tmp09=input("podaj klucz prywanty : ")
        tmp09=tmp09.split(", ")
        for x in tmp09:
            Private_Key.append(int(x))

        # tmp19 = input("podaj klucz publiczny : ")
        # tmp19 = tmp19.split(", ")
        # for x in tmp19:
        #     Public_Key.append(int(x))

        tmp29 = input("podaj kryptogram : ")
        tmp29 = tmp29.split(", ")
        for x in tmp29:
            MSG_final.append(int(x))
        decrypt()
        decrypt_list = []
        spojak = ''
        pmt = 0
        for x in decrypt_binary_list:
            spojak += x
            if pmt == 3:
                decrypt_list.append(spojak)
                spojak = ''
                pmt = -1
            pmt += 1
        spojak = ''
        DESXBinaryToHex = [hex(int(i, 2)).replace("0x", "") for i in decrypt_list]
        for x in DESXBinaryToHex:
            spojak += x
        DESXBinaryToHex.clear()
        DESXBinaryToHex.append(spojak)
        print(DESXBinaryToHex)
        print("Wiadomośc odkodowana to : ", bytes.fromhex(listtostring(DESXBinaryToHex)).decode('utf-8'), end='')
        print("")
        decrypt_binary_list.clear()

















