# Exo 1

##def call (function):
##    function ()
##
##def hello ():
##    print ("hello")
##
##call (hello)

# Exo 2

##def call (*args):
##    return args[0] (args[1],args[2])
##
##def add (a, b) :
##    return a + b

##print (call(add , 2, 9))

# Exo 3

##def call (*args,**kwargs):
##    return args[0] (*args[1:], **kwargs)

##def add (a, b) :
##    return a + b

##def sub (a, b) :
##    return a - b

##def compute (x,y,op=add):
##    return op (x,y)
##print (call( compute , 2 , 9) )
##print (call( compute , 2 , 9 , op= sub )) 

#Exo 1
import time

##def delay(fn):
##    def decorator (f):
##        def wrapper(*args):
##            time.sleep(fn)
##            f(*args)
##        return wrapper
##    return decorator

##@delay (5)
##def printnum(i): 
##    print(i)
    
##cnt = 3 
##while cnt > 0: 
##    printnum(cnt) 
##    cnt -= 1 
##print('KA-BOOM!')

#Exo 1

##def binrep (num):
##    self.__liste =[]
##    while num != 0:
##        result = num%2
##        yield result
##        num = num // 2


##b = binrep (12)
##while True:
##    try:
##        print (next(b))
    
##    except StopIteration:
##        break

#Exo 2

##class Natural:
##    def __init__ (self,num):
##        self.__num = num

##        result = self.__num%2
##        self.__liste =[result]
##        self.__num = self.__num // 2
##        while self.__num != 0:
##            result = self.__num%2
##            self.__liste.append (result)
##            self.__num = self.__num // 2

##    def __getitem__ (self , i):
##        return self.__liste [i]

##    def __len__ ( self ):
##        return len ( self.__liste )

##for e in Natural(42):
##    print (e)

#Exo 3

class NaturalIterator:
    def __init__ (self,bits):
        self.__bits = bits
        self.__index = 0


    def __next__(self ):
        try :
            word = self.__bits[self.__index]
        except IndexError :
            raise StopIteration ()
        self.__index += 1
        return word


class Natural:
    def __init__(self, num):
        self.__num = num
        self.__liste =[]
        while self.__num != 0:
            result = self.__num % 2
            self.__liste.append(result)
            self.__num = self.__num // 2

    def __iter__(self):
        return NaturalIterator(self.__liste)


for e in Natural(42):
    print(e)



