def gcd(a, b):

    # print(a,b,a%b)
    if(b == 0):
        return a
    
    return gcd(b, a%b)

print(gcd(12378, 3054))
# print(gcd(6,10))