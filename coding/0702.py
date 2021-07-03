N! 함수 구현하기

def f(N):
    n = 1
    result = 1
    while n < N:
        n += 1
        result *= n
    return result

def zero(N):
    list = [i for i in str(f(N))]
    Re = list[::-1]
    num = 0
    for i in range(len(Re)+1):
        if Re[i] == '0':
            num += 1
        else: break
    return print(num)

zero(12)

모스 부호 해독

Mos = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}

def interpret(i):

def words(i):
