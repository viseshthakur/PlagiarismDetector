import re,os,sys,collections,math
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
        Attributes : This function accepts File Name as Input

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
        Attributes:This functions accepts two dictionaries! we doing plagarism so we get two different dictionaries for two files

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
        Attributes : It accepts only one dictionary!
        
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
        attributes: It accepts all the .txt files stored in list and also the final where we use final variable for printing for matrix
        
        Function: List of files will be iterated and for every two files the plagiarism is checked and again all the functions will be called.

        return: A list in list called final where values are present.
        
        '''
        
        for i in range(len(files_txt)):
            l=[]
            l.append(files_txt[i])
            for j in range(len(files_txt)):
                if (i==j):
                    l.append('Same')
                else:
                    s1,len1=Bags.FilesToStringToDictionary(files_txt[i])
                    s2,len2=Bags.FilesToStringToDictionary(files_txt[j])
                    if len1=="" and len2=="":
                        l.append('EmptyFile')
                    else:
                        dot=Bags.DotCal(s1,s2)
                        a=Bags.VectorCal(s1)
                        b=Bags.VectorCal(s2)
                        c=round((dot/(a*b))*100,1)
                        l.append(c)
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
    
path=input('Enter the Path')
files = os.listdir(path)
files_txt = [i for i in files if i.endswith('.txt')]
final=[]
q=[]
q.append('FileNames')
for i in files_txt:
    q.append(i)
final.append(q)
final=Bags.BagsOfWordsListFormat(files_txt,final)
z=Bags.matrixPrinting(final)
for i in z:
    print(i)
                    
                      
                     
