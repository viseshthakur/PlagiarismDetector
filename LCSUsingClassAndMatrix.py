import os,sys,re
class LCS(Exception):
        '''
        This Class is used to calculate the Largest Common Subsequence in both the files
        '''
        
        def __init__(self,msg):
                '''
                It is an inititalization to class
                '''
                pass
        
        def FileOperations(f1,f2):
                '''
                attributes:Accpets Two files
                Function: Open the files and removes spaces.
                returns:files in format of string
                '''
                f1= open(f1,"r").read()
                f2= open(f2,"r").read()
                f1=f1.replace(" ","")
                f2=f2.replace(" ","")
                return f1,f2
        def Sequences(f):
                '''
                attributes:Accepts file which changed to string as an input
                Function: It makes a number of combinations of the above file
                returns: it returns the different combinations in form of list
                '''
                l1=[]
                for i in f:
                    s=''
                    for j in range(f.index(i),len(f)):
                        s=s+f[j]
                        l1.append(s)
                return l1
        def ComparingSubStringAndFile(l1,f2):
                '''
                attributes:Accepts the list of different combinations and other file
                Function: for every iteration of element in list check the element is present in other file
                return: it returns only that list whose elements are matched in list and the second file
                '''
                l2=[]
                for i in l1:
                        if i in f2:
                                l2.append(i)
                return l2

        def LCSCalculation(files_txt,final):
                '''
                input:It accepts list of files and a list in list called final for printing matrix
                Function: It is used for calculationg LCS in both files.
                return: It returns a list which has values of lcs of different values.
                '''
                for i in range(len(files_txt)):
                    l=[]
                    l.append(files_txt[i])
                    for j in range(len(files_txt)):
                        if (i==j):
                                l.append('SameFile')
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
                                        l.append('EmptyFiles')
                                else:
                                        a=max(l3)
                                        b=(a*2)/(len1+len2)
                                        b=b*100
                                        l.append(int(b))
                    final.append(l)
                return final
        def matrixPrinting(final):
                '''
                attributes: a list in list is sent as an iput for above function
    
                Functioning: It takes the list and prints the matrix format.
    
                return: it returns list where every value is formated upto with length
    
                '''
                li=[]
                for i in range(len(final)):
                    count=0
                    for j in range (len(final)):
                        if count<len(str(final[i][j])):
                                count=len(str(final[i][j]))
                    li.append(count)
                s=("\t".join('{{:{}}}'.format(n) for n in li))
                z=[s.format(*row) for row in final]
                return z
path=input('enter the path')
files = os.listdir(path)
files_txt = [i for i in files if i.endswith('.txt')]
final=[]
q=[]
q.append('FileNames')
for i in files_txt:
    q.append(i)
final.append(q)
final=LCS.LCSCalculation(files_txt,final)
z=LCS.matrixPrinting(final)
for i in z:
    print(i)
              
