import csv
import datetime

def ssign_in(s_username, s_password):
    l = [s_username.capitalize(), s_password]
    with open("demostu.csv", "r") as fo:
        f = csv.reader(fo)
        u = next(f)
        lu = []
        for i in f:
            lu.append([i[0], i[1]])
    if l in lu:
        return True
    else:
        return False

def tsign_in(t_username, t_password):
    l = [t_username.capitalize(), t_password]
    with open("teach.csv", "r") as fo:
        f = csv.reader(fo)
        u = next(f)
        lu = []
        for i in f:
            lu.append(i)
    if l in lu:
        return True
    else:
        return False

def lsign_in(l_username, l_password):
    li = [l_username.capitalize(), l_password]
    po = ['Usha', 12345]
    if li[0] == po[0] and li[1] == li[1]:
        return True
    else:
        return False

def search_(search):
    with open("book.csv", "r") as fo:
        f = csv.reader(fo)
        l = []
        for i in f:
            if search.capitalize() in i[1] or search.capitalize() in i  and i[6] == "available":
               l.append(i)
            else:
                continue
        return l

def lendd(lend, user, date):
    with open("book.csv", "r") as fo:
        fe = csv.reader(fo)
        l = []
        for i in fe:
            if lend in i:
                i[6] = 'NA'
                i[7] = user
                i[8] = date
                l.append(i)
            else:
                l.append(i)
    with open("book.csv", "w", newline='') as fu:
        f = csv.writer(fu)
        for i in l:
            f.writerow(i)

def lilen():
    with open("book.csv", "r") as fo:
        f = csv.reader(fo)
        l1 = []
        for i in f:
            if i[6] == "available":
               l1.append(i)
        return l1

def given_(given):
    with open("book.csv", "r") as fo:
        fe = csv.reader(fo)
        l = []
        for i in fe:
            if given in i:
                i[6] = 'available'
                i[7] = ''
                i[8] = ''
                l.append(i)
            else:
                l.append(i)
    with open("book.csv", "w", newline='') as fu:
        f = csv.writer(fu)
        for i in l:
            f.writerow(i)

def lile_():
    with open("book.csv", "r") as fo:
        f = csv.reader(fo)
        l1 = []
        for i in f:
            if i[6] == "NA":
               l1.append(i)
        return l1

def stu():
    with open('demostu.csv', 'r') as fi:
        f = csv.reader(fi)
        l=[]
        for i in f:
            l.append(i[0])
        return l

def clas():
    with open('demostu.csv', 'r') as fp:
        f = csv.reader(fp)
        l={}
        for i in f:
            l[i[0]] = i[2]
        return l
    



    