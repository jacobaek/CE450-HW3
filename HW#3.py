Q1
def square(x):
    return x*x
def triple(x):
    return 3*x
def identity(x):
    return x
def increment(x):
    return x+1
def intscts(f, x):
    def compare(s):
        if(f(x)==s(x)):
            return True
        else:
            return False
    return compare
at_three = intscts (square, 3)
print(at_three(triple)) 
print(at_three(increment)) 
at_three = intscts (identity, 1)
print(at_three(square))

Q2
def add(g1, g2):
    def result(x):
        return g1(x)+g2(x)
    return result

identity=lambda x:x
squre=lambda x:x**2
a1= add(identity,squre)
print(a1(4))
a2 = add (a1, identity)
print(a2(4))

Q3
def f():
    def f1():
        def f2(x):
            def f3():
                
                return x
            return f3
        return f2
    return f1

print(f()()(3)())

Q4
def smth(g, dx):
    def f(x):
        
        return (g(x-dx)+g(x)+g(x-dx))/3
    return f

square = lambda x:x**2
print(round(smth(square,1)(0),3))

Q5
def cnt_cd(f):
    def result(n):
        count=0
        for i in range(1,n+1):
            if(f(n,i)):
                count+=1
        return count
    
    return result
def is_prime(n,i):
    if(i==1):
        return 0
    if(i==2):
        return 1
    print("i",i)
    for x in range(2,i):
        if(i%x==0):
            return False
return True



print(cnt_cd (lambda n, i: n % i == 0)(12))
print(cnt_cd (lambda n, i: n % i == 0)(2))
print(cnt_cd (is_prime)(20))

Q6
def card_sum(n):
    a=[]
    result=0
    while True:
        if(n<10):
            a.append(n)
            break
        a.append(n%10)
        n=n//10
    
    for i in range(len(a)-1,-1,-1):
        if(i%2==1):
            
            a[i]=a[i]*2
            if(a[i]>9):
                s1=a[i]%10
                s2=a[i]//10
                a[i]=s1+s2
        result+=a[i]
    return result
print(card_sum (138743))
print(card_sum (5105105105105100))
print(card_sum (4012888888881881))

Q7
from operator  import *
global AO

AO=[]

for i in range(97,123):
    AO.append(chr(i))
for i in range(65,91):
    AO.append(chr(i))

def letter_to_n(x):
    for a in range(0,len(AO)+1):
        if (AO[a]==x):
            return a


def n_to_letter(x):
    return AO[x]
def generator(n, operation):
    def result(letter):
        return AO[operation(letter_to_n(letter),n)]
    
    
    return result

print(letter_to_n('a'))
print(letter_to_n('c'))
print(n_to_letter(3))
h=generator(2,add)
print(h('a'))
h = generator(3, sub)
print(h('d'))

Q8
def add_one(x):
    return x + 1
def times_two(x):
    return x * 2
def add_three(x):
    return x + 3

def cyc(g1, g2, g3):
    def times(count):
        def excute(x):
            a=0
            
            for i in range(0,count):
                
                if(a==0):
                    x=add_one(x)
                if(a==1):
                    x=times_two(x)
                if(a==2):
                    x=add_three(x)
                if(a%3==0 and i!=0):
                    x=add_one(x)
                if(a>2):
                    a=a%3
                
                
                a=a+1
            return x
        return excute
    return times


my_cyc = cyc(add_one, times_two, add_three)
h= my_cyc(0)
print(h(5))
h = my_cyc(6)
print(h(1))
h = my_cyc(3)
print(h(2))

