'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

def fastPower(a,b,n):
    res = 1 
    while b>0:
        if ((b&1)!=0):
            res= (res%n * a%n) % n
        
        a = (a%n * a%n)%n
        b = b>>1
        
    return res
    
    
a = int(input("Enter:"))
b = int(input("Enter:"))
n = 10000000007
print(fastPower(a,b,n))