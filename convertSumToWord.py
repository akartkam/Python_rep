def TriplToWord(triplet):
    sot = ('','сто','двести','триста','четыреста','пятьсот','шестьсот','семьсот','восемьсот','девятьсот')
    des = ('','','двадцать','тридцать','сорок','пятьдесят', 'шестьдесят','семьдесят','восемьдесят','девяносто')
    edin = ('','один','два','три','четыре','пять','шесть','семь', 'восемь','девять','десять',\
            'одиннадцать', 'двенадцать',  'тринадцать','четырнадцать','пятнадцать',   'шестнадцать',\
            'семнадцать','восемнадцать','девятнадцать')
    s = ''
    triplet = triplet % 1000
    if triplet > 99 :
        s = sot[triplet // 100] + ' '
        triplet = triplet % 100

    if triplet > 19 :
        s = s + des[triplet // 10] + ' '
        triplet = triplet % 10

    return s + edin[triplet]


def SumToWord(summa):
    if summa == 0:
        return 'Ноль руб. 00 коп.'
    intSum = int(summa)
    wordSum = ''
    if intSum > 999999999:
        divSum =  intSum // 1000000000
        wordSum = TriplToWord(divSum)
        if ((divSum-(divSum // 100)*100)>10) and ((divSum-(divSum // 100)*100)<20):
            wordSum += ' миллиардов'
        elif (divSum % 10) == 1:
            wordSum += ' миллиард'
        elif ((divSum % 10)>=2)and((divSum % 10)<=4):
            wordSum += ' миллиарда'
        else:
            wordSum += ' миллиардов'
        intSum = intSum % 1000000000

    if intSum > 999999:
        divSum =  intSum // 1000000
        wordSum += ' ' + TriplToWord(divSum)
        if ((divSum-(divSum // 100)*100)>10) and ((divSum-(divSum // 100)*100)<20):
            wordSum += ' миллионов'
        elif (divSum % 10) == 1:
            wordSum += ' миллион'
        elif ((divSum % 10)>=2)and((divSum % 10)<=4):
            wordSum += ' миллиона'
        else:
            wordSum += ' миллионов'
        intSum = intSum % 1000000

    if intSum > 999:
        divSum =  intSum // 1000
        wordSum += ' ' + TriplToWord(divSum)
        if ((divSum-(divSum // 100)*100)>10) and ((divSum-(divSum // 100)*100)<20):
            wordSum += ' тысяч'
        elif (divSum % 10) == 1:
            wordSum = wordSum[:-2]
            wordSum += 'на тысяча'
        elif (divSum % 10) == 2:
              wordSum = wordSum[:-1]
              wordSum += 'е тысячи'
        elif ((divSum % 10)>=3)and((divSum % 10)<=4):
              wordSum += ' тысячи'
        else:
            wordSum += ' тысяч'
        intSum = intSum % 1000
    
    divSum = intSum
    wordSum += ' ' + TriplToWord(divSum) + ' руб.'
    strsumma = str(summa).replace(',','.') 
    divSum = int(strsumma[strsumma.find('.')+1:])
    wordSum += ' ' + str(divSum) + ' коп.'
    wordSum = wordSum.strip()
    wordSum = wordSum[0:1].upper() + wordSum[1:]
    return wordSum
            

    


if __name__ == '__main__':
    while True:
        try:
            x = float(input("Введите, пожалуйста, сумму , меньше 1 триллиона число: "))
            print(SumToWord(x))
        except:
            print("Ой!  Это некорректное число.  Попробуйте ещё раз...")
            
