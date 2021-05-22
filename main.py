import random
import math


def is_prime(a):
    if a == 2:
        return True
    elif (a < 2) or ((a % 2) == 0):
        return False
    elif a > 2:
        for i in range(2, a):
            if not (a % i):
                return False
    return True


def CheckIfProbablyPrime(x):
    return pow(2, x - 1, x) == 1


a = int(input("Write A: "))
p = int(input("Write P: "))

check_a = is_prime(a)
check_p = is_prime(p)


while (check_a == False) or (check_p == False):
    a = int(input("Enter a prime number for A: "))
    p = int(input("Enter a prime number for P: "))
    check_p = is_prime(a)
    check_q = is_prime(p)

Xa = int(input("Secret number Xa: "))
Xb = int(input("Secret number Xb: "))
if 1 <= Xa <= p - 1 and 1 <= Xb <= p - 1:
    Ya = pow(a, Xa, p)
    print("Ya: ", Ya)
    Yb = pow(a, Xb, p)
    print("Yb: ", Yb)

    kA = pow(Yb, Xa, p)
    print("kA: ", kA)
    kB = pow(Ya, Xb, p)
    print("kB: ", kB)

else:
    print("(Xa or Xb) <1 or >p-1")
