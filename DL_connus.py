from DL import DL
from math import factorial
from fractions import Fraction as F


def DL_exp(n):
    return DL([f"1/{factorial(k)}" for k in range(n+1)])

def DL_cos(n):
    return DL([f"1/{(-1)**(k//2)*factorial(k)}" if k%2 == 0 else 0 for k in range(n+1)])

def DL_sin(n):
    return DL([f"1/{(-1)**((k-1)//2)*factorial(k)}" if k%2 == 1 else 0 for k in range(n+1)])

def DL_ch(n):
    return DL([f"1/{factorial(k)}" if k%2 == 0 else 0 for k in range(n+1)])

def DL_sh(n):
    return DL([f"1/{factorial(k)}" if k%2 == 1 else 0 for k in range(n+1)])

def DL_ln(n):
    return DL([0] + [f"1/{(-1)**(k-1)*k}" for k in range(1, n+1)])

def DL_puissance(a, n):

    def facteur(a, k): # Des bisous Aurélien
        r = 1
        for i in range(k):
            r *= a-i
        return r

    return DL([facteur(a, k)/factorial(k) for k in range(n+1)]) # Renvoie un float au début, à corriger

def DL_inverse(n):
    return DL([f"{(-1)**k}" for k in range(n+1)])


if __name__ == "__main__":
    print(DL_exp(5))
    print(DL_cos(5))
    print(DL_sin(5))
    print(DL_ch(5))
    print(DL_sh(5))
    print(DL_ln(5))
    print(DL_puissance(F(1, 2), 5))
    print(DL_inverse(5))