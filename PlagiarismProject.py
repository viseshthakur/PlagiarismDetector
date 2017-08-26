print('------------Bag of Words------------')
import re,os,sys,collections,math,re
class Bags:
    '''
    This Class is uded to caclculate Bag of words module in Plagiarism
    It has many functions and the main aim is to calculate plagiarism of different files.
    '''
    def __init__(self,msg):
        '''
        A basic initialisation for our class
        '''
        pass
    
    def FilesToStringToDictionary(f1):
        '''
        Arguments : This function accepts File Name as Input

        Functioning: It converts our files into dictionaries

        Return : This function returns dictionary and also string of whole file!
        '''
        file = open(f1,"r").read().lower()
        p= re.sub('[^a-zA-Z0-9\n\_\ ]',"",file)
        s=p.split(" ")
        count=collections.Counter(s)
        return count,p
    
    def DotCal(di,di1):
        '''
        Arguments:This functions accepts two dictionaries! we doing plagarism so we get two different dictionaries for two files

        Function: It checks for key in both dictionaries and calculate the dot product by multiplying values of keys

        return: We get Dot Product!which we will return back
        
        '''
        dot=0
        for k in di:
            if k in di1:
                dot=dot+(di.get(k)*di1.get(k))
        return dot
    
    def VectorCal(di):
        '''
        Arguments: It accepts only one dictionary!
        
        Function: Calculating vector of of dictionary by using values of it
                     
        return: For every dictionary it returns vector of the dictionary values
        '''
        vect1=0
        for k in di:
            vect1=vect1+(di.get(k)**2)
        vect1=math.sqrt(vect1)
        return vect1
    
    def BagsOfWordsListFormat(files_txt,final):
        '''
        Arguments: It accepts all the .txt files stored in list and also the final where we use final variable for printing for matrix
        
        Function: List of files will be iterated and for every two files the plagiarism is checked and again all the functions will be called.

        return: A list in list called final where values are present.
        
        '''
        
        for i in range(len(files_txt)):
            l=[]
            l.append(files_txt[i])
            for j in range(len(files_txt)):
                if (i==j):
                    l.append(0)
                else:
                    s1,len1=Bags.FilesToStringToDictionary(files_txt[i])
                    s2,len2=Bags.FilesToStringToDictionary(files_txt[j])
                    if len1=="" and len2=="":
                        l.append(0)
                    else:
                        dot=Bags.DotCal(s1,s2)
                        a=Bags.VectorCal(s1)
                        b=Bags.VectorCal(s2)
                        c=round((dot/(a*b))*100,1)
                        l.append(c)
            final.append(l)
        return final
#You'll enter the Path
path=input('Enter the Path')
files = os.chdir(path)
list=os.listdir()
files_txt = [i for i in list if i.endswith('.txt')]
final=[]
q=[]
q.append('FileNames')
for i in files_txt:
    q.append(i)
final.append(q)
final=Bags.BagsOfWordsListFormat(files_txt,final)
#Matrix Printing
print('\n'.join(['   '.join(['{:10}'.format(j) for j in row])  for row in final]))

print('-----------------------LCS------------------------')
                     
class LCS:
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
                                l.append(0.0)
                        elif i<j:
                                l.append(0.0)
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
                                        l.append(0)
                                else:
                                        if len(l3)==0:
                                                l.append(0)
                                        else:
                                                a=max(l3)
                                                b=((a*2)/(len1+len2))*100
                                                l.append(round(b,1))
                    final.append(l)
                return final
files = os.chdir(path)
files_txt = [i for i in os.listdir() if i.endswith('.txt')]
final=[]
q=[]
q.append('FileNames')
for i in files_txt:
    q.append(i)
final.append(q)
final=LCS.LCSCalculation(files_txt,final)
print('\n'.join(['   '.join(['{:10}'.format(j) for j in row])  for row in final]))                    

              
