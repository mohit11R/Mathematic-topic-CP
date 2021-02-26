

def isPrime(n):
    boolean = [True]*(n+1) 
    boolean[0] = False
    boolean[1] = False
    
    
    for i in range(2,int(n**1/2)):
        for j in range(2*i,n+1,i):
            boolean[j] = False
    
    return boolean
    

n = int(input("Enter:"))
v = isPrime(n)
for z in range(len(v)):
    print("{} {}".format(z,v[z]))
    