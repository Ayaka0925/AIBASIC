# import math as mt

# import statistics as st

# x = mt.pow(2,3)
# print(x)
# y = [1,2,3,4,5,6,6,6,7,8,8,8]

# print(st.mean(y))

# from model import model
#1こだけ
# from model.model import module2

# print(module2())


# from model import model
import csv

datas = open('data/book.csv','r')
print(datas)
# with open('data/book.csv','r') as rf:
#     reader = csv.reader(rf)
#     #header を除く
#     header = next(reader)

#     #header表示したければ
#     # print(header)

#     for row in reader:
#         body.append(row)

# with open('data/book.csv','r') as rf:
#     reader = csv.reader(rf)
#     header = next(reader)

#     for rows in reader:
#         print(rows)

# name = input('Enter the bonk name:')
# author = input('enter the author:')
# isbn = input('enter isbn:')
# body.append([len(body)+1,name,author,isbn])

# # header = ['id','name','author','isbn']
# # body = [
# #     ['1','python101','Jan','123456'],
# #     ['2','python102','Jan','678899']
# # ]

# with open('data/book.csv','w') as wf:
#     writer = csv.writer(wf)
#     writer.writerow(header)
#     writer.writerows(body)


from model.model import readData
data = readData('data/book.csv')

name = input('Enter the bonk name:')
author = input('enter the author:')
isbn = input('enter isbn:')
data.append([len(data)+1,name,author,isbn])

from model.model import writeData
writeData('data/book.csv',data)