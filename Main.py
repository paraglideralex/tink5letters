liss=[]
lin=''
k=0
with open('RU2.txt', 'r', encoding="utf-8") as lorem_ipsum_text:
    for line in lorem_ipsum_text:
        k+=1
        lin = (line)
        if len((lin)) == 6:
            liss.append(lin)
# print(liss)
p=0
with open('OUT.txt', 'w', encoding="utf-8") as out_text:
    for line in liss:
        print(line, file=out_text,end='')
        p+=1

print (f'Конец, отобрано {p} слов из {k}')



