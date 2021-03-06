'''
Created on Dec 22, 2016

@author: bogdan
'''
from domain.book import *
from repo.RepositoryException import *
from algorithm.iterableDS import *

class BookRepository:
    def __init__(self):
        self.__arr=IterableDS()
    
    def __len__(self):
        return len(self.__arr)
    
    def get(self,ind):
        return self.__arr[ind]
    
    def getAll(self):
        return self.__arr
    
    def delete(self,ind):
        return self.__arr.pop(ind)
    
    def add(self,ID,title,description,author):
        if(self.isAvailable(ID)==False):
            raise RepositoryException("ID="+str(ID)+" is already used!")
        self.__arr.append(book(ID,title,description,author))
        
    def __str__(self):
        s=""
        for it in self.__arr:
            s+=str(it)
            s+='\n'
        if(s==""):
            s="The list is empty!\n"
        return s
    
    def isAvailable(self,ID):
        for it in self.__arr:
            if(it.getID()==ID):
                return False
        return True

