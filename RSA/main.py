
from random import randrange, getrandbits
import random
import hashlib


def calculateN(numberP, numberQ):
    return numberP*numberQ


def calculateO(numberP, numberQ):
    return (numberP-1)*(numberQ-1)


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True




def calculatePossibleE(numberP, numberQ):
    listE = []
    x = 1

    b = calculateO(numberP, numberQ)
    x = b - 1000
    print(b)
    while x < b:
        if x % b != 0 and isPrime(x):
            listE.append(x)
        x += 1
    return listE

def gcd(a, b):
        while a > 0:
            b=b % a
            (a, b)=(b, a)
        return b

def hcfnaive(a, b):
    if(b==0):
        return a
    else:
        return hcfnaive(b, a % b)


def carmichael(n):
    coprimes = [x for x in range(1, n) if hcfnaive(x, n) == 1]
    k = 1
    while not all(pow(x, k, n) == 1 for x in coprimes):
        k += 1
    return k

def generatePrivateKey(numberP, numberQ, numberE):
    # b=carmichael(calculateN(numberP, numberQ))
    b = calculateO(numberP, numberQ)
    return pow(numberE, -1, b)

def messageCalcualator(letter):
    return ord(letter)

def inverseMessageCalculator(letter):
    return chr(letter)


def encrypt(messageEncrypt, numberP, numberQ, numberE):
    listX =[]
    N=calculateN(numberP, numberQ)
    for x in messageEncrypt:
        # print("co tam")
        b =int(messageCalcualator(x))
        x=pow(b, numberE, N)
        listX.append(x)
    return listX

def decrypt(encryptedMessage, privateKey, NumberN):
    tmp=""
    for x in encryptedMessage:
       tmp += inverseMessageCalculator(pow(int(x), privateKey, NumberN))
    return tmp


first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]


def nBitRandom(n):
    return random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)


def getLowLevelPrime(n):
    while True:
        pc = nBitRandom(n)

        for divisor in first_primes_list:
            if pc % divisor == 0 and divisor ** 2 <= pc:
                break
        else:
            return pc


def isMillerRabinPassed(mrc):
    maxDivisionsByTwo = 0
    ec = mrc - 1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert (2 ** maxDivisionsByTwo * ec == mrc - 1)

    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2 ** i * ec, mrc) == mrc - 1:
                return False
        return True

    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True






#
# if __name__ == '__main__':
#     while True:
#         n = 1024
#         prime_candidate = getLowLevelPrime(n)
#         if not isMillerRabinPassed(prime_candidate):
#             continue
#         else:
#             print(n, "bit prime is: \n", prime_candidate)
#             P=prime_candidate
    #         break
    # while True:
    #     n = 1024
    #     prime_candidate = getLowLevelPrime(n)
    #     if not isMillerRabinPassed(prime_candidate):
    #         continue
    #     else:
    #         print(n, "bit prime is: \n", prime_candidate)
    #         Q = prime_candidate
    #         break
    # while True:
    #     n = 1024
    #     prime_candidate = getLowLevelPrime(n)
    #     if not isMillerRabinPassed(prime_candidate):
    #         continue
    #     else:
    #         x = calculateO(P, Q)
    #         if prime_candidate < x and prime_candidate % x != 0:
    #             print(n, "bit prime is: \n", prime_candidate)
    #             E = prime_candidate
    #             print(E)
    #             break



























wybor = 1
while wybor !=0:
    print("0- koniec")
    print("1-encrypcja")
    print("2-dekrypcja")
    wybor = int(input("Wpisz co chesz zrobić : "))
    if(wybor==1):
        # P = int(input("Insert First Prime Number P : "))
        # Q = int(input("Insert Second Prime Number Q : "))
        P=7000061
        Q=7001287
        # print(calculatePossibleE(P, Q))
        # E = int(input("Choose e From List Above : "))
        E = 49009422076187
        print("Public Key is : (", calculateN(P, Q), ",", E, ")")
        print("Private Key is : ", generatePrivateKey(P, Q, E))
        message = input("Insert message to be encrypted : ")
        m1=hashlib.sha1(message.encode())
        m1 = m1.hexdigest()
        print(m1)
        m1 = str(m1)
        print("N value is : ", calculateN(P, Q))
        print("Zaszyfrowana wiadomośc to : ", encrypt(m1, P, Q, E))
        print("Jesli chesz sprawdzić czy podpis sie zgadza to wpisz 3 ")
        wybor = int(input())
        if wybor == 3:
            tmp12 = encrypt(m1, P, Q, E)
            zmienna = decrypt(tmp12, generatePrivateKey(P, Q, E), calculateN(P, Q))
            if(zmienna == m1) :
                print("podpis poprawny")


    elif(wybor==2):
        encryptedMessage = input("Podaj szyfrogram : ")
        N = int(input("Podaj N : "))
        PrivateKey = int(input("Podaj klucz prywatny : "))
        encryptedMessage = encryptedMessage.split(", ")
        print(decrypt(encryptedMessage, PrivateKey, N))
        m1=input("Wiadmość : ")
        m2 = hashlib.sha1(m1.encode())
        m2 = m2.hexdigest()
        c1 = decrypt(encryptedMessage, PrivateKey, N)
        if (c1 == m2):
            print("podpis poprawny")

