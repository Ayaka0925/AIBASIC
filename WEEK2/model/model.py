# def module1():
#     return 'Hello World'

# def module2():
#     return 'I am module2'
import csv

def readData(path):  
    
    body =[]
    with open('data/book.csv','r') as rf:
        reader = csv.reader(rf)
        # header = next(reader)

        for row in reader:
            body.append(row)
        return body

def writeData(path,data):
    header = ['id','name','author','isbn']
    with open('data/book.csv','w') as wf:
        writer = csv.writer(wf)
        writer.writerow(header)
        writer.writerows(data)