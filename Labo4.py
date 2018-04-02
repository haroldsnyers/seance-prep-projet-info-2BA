# Exo 1.1
def call(a):
    a()
#   return a()

def hello():
    print("hello")

call(hello)
print("")


# Exo 1.2
def call1(*args):
    return args[0](args[1], args[2])

def add1(a, b):
    return a + b

print(call1(add1, 2, 9))
print("")


# Exo 1.3

def call2 (*args,**kwargs):
    return args[0] (*args[1:], **kwargs)

def add2(a, b) :
    return a + b

def sub2(a, b) :
    return a - b

def mult2(a, b):
    return sub2(a, b) * add2(a, b)

def compute2(x, y, op=add2):
    return op(x, y)

print(call2(compute2, 2, 9))
print(call2(compute2, 2, 9, op=sub2))
print(call2(compute2, 2, 9, op=mult2))
print("")

# Exo 2.1
import time

def delay(fn):
    def decorator(f):
#       a = 1
        def wrapper(*args):
            time.sleep(fn)
            f(*args)

#           t1 = time.time()
#           while (time.time()-t1) < a:
#              pass
#           return fn(*args)

        return wrapper
    return decorator

@delay (2)
def printnum(i):
    print(i)
    
cnt = 3
while cnt > 0:
    printnum(cnt)
    cnt -= 1
print('KA-BOOM!')
print("")

# Exo 3.1
def binrep(x):
    while x != 0:
        result = x % 2
        yield result
        x = x//2


b = binrep(12)

while True:
    try:
        print(next(b))
    except StopIteration:
        break

print("")

# Exo 2

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

# Exo 3

class NaturalIterator:
    def __init__(self, bits):
        self.__bits = bits
        self.__index = 0

    def __next__(self):
        try:
            word = self.__bits[self.__index]
        except IndexError:
            raise StopIteration()
        self.__index += 1
        return word


class Natural:
    def __init__(self, num):
        self.__num = num
        self.__liste = []
        while self.__num != 0:
            result = self.__num % 2
            self.__liste.append(result)
            self.__num = self.__num // 2

    def __iter__(self):
        return NaturalIterator(self.__liste)


for e in Natural(42):
    print(e)



