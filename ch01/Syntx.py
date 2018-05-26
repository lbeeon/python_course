# -*- coding: UTF-8 -*-
import csv

def ReadFile(file_name):
    with open(file_name) as csvfile:
        # rows = csv.DictReader(csvfile)
        rows = csv.reader(csvfile)
        # rows = csv.reader(csvfile)
        for row in rows:
            print(row)

def Add(a, b):
    return a+b


if __name__ == '__main__':
    total = Add(1, 3)
    print type(total)
    print total
    ReadFile('test.csv')

