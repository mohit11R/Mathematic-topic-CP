
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


a = int(input("Enter:"))
b = int(input("Enter:"))
print(gcd(a,b))