import re
import Functions
liss=[]
lin=''
k=0
with open('OUT.txt', 'r', encoding="utf-8") as lorem_ipsum_text:
    for line in lorem_ipsum_text:
        liss.append(line)
        k+=1

letter1 = '[^неамтв]'
letter2 = '[^неамтво]'
letter3 = '[р]'
letter4 = '[^неамтвки]'
letter5 = '[^неамтв]'
total = 'ркои'
p=0
lsout=[]
with open('ChOUT.txt', 'w', encoding="utf-8") as outt:
    for line in liss:
        if         (re.match(letter1, line[0]) and re.match(letter2, line[1])
                and re.match(letter3, line[2]) and re.match(letter4, line[3])
                and re.match(letter5, line[4]) and Functions.InStr(total, line)):
            print(line, file=outt, end='')
            lsout.append(line)
            p += 1

for ls in lsout:
    print(ls,end='')
print(f'нашёл {p} совпад. по паттерну из {k} в базе данных')