import random
from Crypto.Util import number
import math

p = number.getPrime(5)
q = number.getPrime(5)
print (p,q)

n = p*q

phi = (p-1)*(q-1)

coprime = []
for i in range(0,32,1):
    if (math.gcd(i,phi) == 1):
                coprime.append(i)
e = random.choice(coprime)
print ("Encryption key is " +str(e))

mulinv = []
for i in range(phi):
        if ((i*e)%phi == 1):
            mulinv.append(i)
d = mulinv[0]
print ("Decryption key is "+str(d))

message = 10
encryption = math.pow(message,e)%n
print (int(encryption))

try :
    decryption = math.pow(encryption,d)%n
except OverflowError :
    decryption = math.pow(long(encryption),d)%n
print (decryption)

# Brute Forcing the RSA algorithm
# Given encryption, e and n we have to brute force to get d and hence Decryption
for i in range(phi):
    decryption = math.pow(encryption,i)%n
    if decryption == message:
        print ("Brute Force Successful, message is "+str(message))

