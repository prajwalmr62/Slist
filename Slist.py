""" 
slist ver 1.0 
github repository: prajwalmr62 
slist is a new class which is extended version of the default list type. 
Modifications: 
sort: 
This list, sorts using the size of the elements and within same type of elements, upon their values. 
size: 
creates property size list and prints the size of elements 
""" 

import sys 
class slist(list): 
    def sort(self): 
        for i in range(0,len(self)): 
            for j in range(0,i): 
                if sys.getsizeof(self[i])<sys.getsizeof(self[j]): 
                    self[i],self[j]=self[j],self[i] 
                if (sys.getsizeof(self[i])==sys.getsizeof(self[j]) and type(self[i]) == type(self[j])): 
                    if(self[i]<self[j]): 
                        self[i],self[j]=self[j],self[i] 
    def size(self): 
        size=[] 
        for i in range(0,len(self)): 
            size.append(sys.getsizeof(self[i])) 
        print(size)
