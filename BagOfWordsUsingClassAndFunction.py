import re
import os
import sys
class Bags:
    def __init__(self,msg):
        pass
    def StrToList(f1,f2):
        file = open(f1,"r")
        x=file.read()
        p=x.lower()
        p= re.sub('[^a-z\ \']+', "",p)
        s1=p.split(" ")
        file = open(f2,"r")
        y=file.read()
        y=y.lower()
        y= re.sub('[^a-z\ \']+', "",y)
        s2=y.split(" ")
        return s1,s2
    def LtoD(s1,s2):
        di={}
        for i in range(len(s1)):
            di[s1[i]]=s1.count(s1[i])
        di1={}
        for i in range(len(s2)):
            di1[s2[i]]=s2.count(s2[i])
        return di,di1
    def DotCal(di,di1):
        dot=0
        for k in di:
            if k in di1:
                dot=dot+di.get(k)*di1.get(k)
        return dot
    def VectorCal(di,di1):
        vect1=0
        for k in di:
            vect1=vect1+di.get(k)**2
        vect1=vect1**(1/2)
        vect2=0
        for k in di1:
            vect2=vect2+di1.get(k)**2
        vect2=vect2**(1/2)
        return vect1*vect2
cwd = os.getcwd()
files = os.listdir(cwd)
files_txt = [i for i in files if i.endswith('.txt')]
#l=["first.txt","second.txt","third.txt","four.txt","five.txt"]
for i in files_txt:
    for j in files_txt:
        if (files_txt.index(i)<=files_txt.index(j)):
            pass
        else:
            s1,s2=Bags.StrToList(i,j)
            di,di1=Bags.LtoD(s1,s2)
            dot=Bags.DotCal(di,di1)
            a=Bags.VectorCal(di,di1)
            b=(dot/a)*100
            print("Plagiarism of ",i , " with" , j, " is ",b,'%')
