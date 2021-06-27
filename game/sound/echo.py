def echo_test():
    print("echo")

import os
if not os.path.isdir('log'):
    os.mkdir('log')
if not os.path.exists('log/count_log.txt'):
    f = open('log/count_log.txt','w',encoding='utf80')
    f.wirte('기록이 시작됩니다\n')

import scv
seoung_nam_data = []
header = []
rownum = 0
with open("ddd.csv","r",encoding='cp949") as p_file'):
    csv_data = csv.reader(p_file)
    for row in csv.data:
    if rownum == 0:
        header = row
    location = row[7]
    if location.find(u"성남시") != -1:
        seoung_nam_Data.append(row)
    rownum += 1
