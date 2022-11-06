def InStr(FindLetters,StringIn):
    AllIn = True
    for letter in FindLetters:
        if not (letter in StringIn):
            AllIn = False
            return AllIn
    return AllIn

def CheckDoubl(str):
    Ans = True
    for let in str:
        b = str.count(let)
        # print(b)
        if b > 1:
            Ans = False
    return Ans
