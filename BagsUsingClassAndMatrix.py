import re,os,sys,collections
class Bags:
    def __init__(self,msg):
        pass
    def StrToList(f1):
        file = open(f1,"r").read().lower()
        p= re.sub('[^a-zA-Z0-9\n\_\ ]',"",file)
        s=p.split(" ")
        count=collections.Counter(s)
        return count
    def DotCal(di,di1):
        dot=0
        for k in di:
            if k in di1:
                dot=dot+(di.get(k)*di1.get(k))
        return dot
    def VectorCal(di):
        vect1=0
        for k in di:
            vect1=vect1+(di.get(k)**2)
        vect1=vect1**(1/2)
        return vect1
files = os.listdir(os.getcwd())
files_txt = [i for i in files if i.endswith('.txt')]
final=[]
for i in range(len(files_txt)):
    l=[]
    for j in range(len(files_txt)):
        if (i<=j):
            l.append(0)
        else:
            s1=Bags.StrToList(files_txt[i])
            s2=Bags.StrToList(files_txt[j])
            dot=Bags.DotCal(s1,s2)
            a=Bags.VectorCal(s1)
            b=Bags.VectorCal(s2)
            c=(dot/(a*b))*100
            l.append(int(c))
            #print("Plagiarism of ",i , " with" , j, " is ",c,'%')
    final.append(l)
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in final]))
