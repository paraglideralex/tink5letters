import Functions

liss=[]
let1=""
let2=""
let3=""
let4=""
let5=""

str1='абвгдежзийклмнопрстуфхцчшщъыьэюя'
str2='абвгдежзийклмнопрстуфхцчшщъыьэюя'
str3='абвгдежзийклмнопрстуфхцчшщъыьэюя'
str4='абвгдежзийклмнопрстуфхцчшщъыьэюя'
str5='абвгдежзийклмнопрстуфхцчшщъыьэюя'

with open('OUT.txt', 'r', encoding="utf-8") as lorem_ipsum_text:
    for line in lorem_ipsum_text:
        let1+=line[0]
        let2+=line[1]
        let3+=line[2]
        let4+=line[3]
        let5+=line[4]
        liss.append(line)
liss.pop(-1)

print(liss)
Dict1={}
Dict2={}
Dict3={}
Dict4={}
Dict5={}

for let in str1:
    Dict1[let]=let1.count(let)
    Dict2[let]=let2.count(let)
    Dict3[let]=let3.count(let)
    Dict4[let]=let4.count(let)
    Dict5[let]=let5.count(let)
print(Dict1)
print(Dict2)
print(Dict3)
print(Dict4)
print(Dict5)
Wordss={}

# если нужно отсеять первое слово
for let in 'порка':
    Dict1[let]=0
    Dict2[let]=0
    Dict3[let]=0
    Dict4[let]=0
    Dict5[let]=0

for word in liss:
    if Functions.CheckDoubl(word):
        # print (lett)
        Wordss[word]=Dict1[word[0]]
        Wordss[word]+=Dict2[word[1]]
        Wordss[word]+=Dict3[word[2]]
        Wordss[word]+=Dict4[word[3]]
        Wordss[word]+=Dict5[word[4]]

# dict(sorted(Wordss.items()))
with open('Sort.txt', 'w', encoding="utf-8") as out_text:
    for key , val in Wordss.items():
        # print(key, file=out_text, end='')
        # print(key + '  \t  '+str(val), file=out_text, end='')
        print(val, file=out_text, end='\n')



