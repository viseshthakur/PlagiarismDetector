import os,sys,re
class LCS(Exception):
        def __init__(self,msg):
                pass
        def FileOperations(f1,f2):
                f1= open(f1,"r").read()
                f2= open(f2,"r").read()
                f1=f1.replace(" ","")
                f2=f2.replace(" ","")
                return f1,f2
        def Sequences(f):
                l1=[]
                for i in f:
                    s=''
                    for j in range(f.index(i),len(f)):
                        s=s+f[j]
                        l1.append(s)
                return l1
        def ComparingSubStringAndFile(l1,f2):
                l2=[]
                for i in l1:
                        if i in f2:
                                l2.append(i)
                return l2
files = os.listdir(os.getcwd())
files_txt = [i for i in files if i.endswith('.txt')]
final=[]
for i in range(len(files_txt)):
    l=[]
    for j in range(len(files_txt)):
        if (i==j):
                l.append('Same')
        elif i<j:
                l.append('Repeat')
        else:
                f1,f2=LCS.FileOperations(files_txt[i],files_txt[j])
                l1=LCS.Sequences(f2)
                l2=LCS.ComparingSubStringAndFile(l1,f1)
                len1=len(f1)
                len2=len(f2)
                l3=[]
                for k in l2:
                        l3.append(len(k))
                if len(f1)==0 and len(f2)==0:
                        l.append(100)
                else:
                        a=max(l3)
                        b=(a*2)/(len1+len2)
                        b=b*100
                        l.append(int(b))
    final.append(l)
print('',files_txt)
print('\n'.join([((' ')*(10)).join(['{:5}'.format(item) for item in row])for row in final]))

