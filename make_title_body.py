# coding:utf-8
import re
pattern = r'^\[\[.+\]\]$'
repat = re.compile(pattern)

#text = '[[ アンパサンド ]]'
#if repat.match(text):
#    print('ok')


titles = []
bodys = []
body = []
with open('jawiki-latest-pages-articles.xml-001.txt_mod', 'r') as f: 
    for raw_line in f:
        #line = raw_line[:-2]
        line = raw_line.strip(' \n')
#        print(line)
        if repat.match(line):
            if body != []:
                bodys.append(body)
                body = []
            titles.append(line.replace(' ', '')[2:-2])
        elif line == '':
            continue
        else:
#            print(line)
            line = line.replace('[','').replace(']','')
            line = line.replace('"','').replace("'",'')
            line = line.replace('*','').replace('、','')
            line = line.replace('(','').replace(')','')
            line = line.replace('（','').replace('）','')
            line = line.replace('=','')
            line = line.split(' ')
#            print(line)
            while line.count('') > 0:
                line.remove('')
            print(line)
            body += line
           # body.append(line.split(' ').remove(''))

    bodys.append(body)

#print(len(titles))
#print(len(bodys))
#
#print(titles[0])
#print(bodys[0])
#print(' '.join(bodys[0]))
#print(bodys[0])


f = open('title.txt', 'w')
for title in titles:
    f.write(title + '\n')
f.close()

f = open('body.txt', 'w')
for body in bodys:
    f.write(' '.join(body) + '\n')
f.close()
