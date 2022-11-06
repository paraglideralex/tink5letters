def InStr(FindLetters,StringIn):
    '''
    Проверяет вхождение в строку всех заданных букв в поисковой строке

    :param FindLetters: string, буквы, наличие которых надо проверить
    :param StringIn: string – строка, в которой надо проверить наличие букв из FindLetters
    :return: bool – входят ли все буквы из поисковой строки, или нет
    '''
    AllIn = True
    for letter in FindLetters:
        if not (letter in StringIn):
            AllIn = False
            return AllIn
    return AllIn

def CheckDoubl(str):
    '''
    Проверяет наличие дубликатов в строке

    :param str: string – входная строка для анализа на дубликаты
    :return: bool – булево значение, есть дубликаты или нет
    '''
    Ans = True
    for let in str:
        b = str.count(let)
        # print(b)
        if b > 1:
            Ans = False
    return Ans
