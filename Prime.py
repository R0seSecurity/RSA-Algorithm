import sympy
import math
def prime_generation(x, y):
    # generates random prime number between lower and upper limit
    p = sympy.randprime(x, y)
    q = sympy.randprime(x, y)
    n = p * q
    phiN = (p - 1) * (q - 1)
    print(f"p: {p}, q:{q}, n:{n}, phiN: {phiN}")
    return phiN

def encrypted_key():
    e = sympy.randprime(11, phin)
    while e < phin:
        if math.gcd(e, phin) == 1:
            encryptedKey = e
            break
        e = sympy.randprime(11, phin)
    return encryptedKey


def GCD(x, y):
    if (y == 0):
        return x
    if (x == y):
        return x
    return GCD(y, x % y)


def decryption(e, phi):
    d = pow(e, -1, phi)

    return d


phin = prime_generation(32768, 65536)
e_key = encrypted_key()
print(f"The encryption key 'e' is {e_key}")

decrypted_key = decryption(e_key, phin)
print(f"The decryption key 'd' is {decrypted_key}")