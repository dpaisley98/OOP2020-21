from math import *


class Illegal(Exception):
    pass


def Euclid(verbose=True):
    x = input("Give a value for X:")
    y = input("Give a value for Y:")
    if x < y:  # We want x >= y
        print()

    while y != 0:
        if verbose:
            print('%s = %s * %s + %s' % (x, floor(int(x) / int(y)), y, int(x) % int(y)))
        (x, y) = (y, int(x) % int(y))
    if verbose:
        print('gcd is %s' % x)
    return


def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

    # To compute x^y under modulo m


def power(x, y, m):
    if (y == 0):
        return 1
    p = power(x, y // 2, m) % m
    p = (p * p) % m

    return p if (y % 2 == 0) else (x * p) % m


# Function to find modular
# inverse of a under modulo m
# Assumption: m is prime
def modInverse(a, m):
    if (__gcd(a, m) != 1):
        print("Inverse doesn't exist")

    else:

        # If a and m are relatively prime, then
        # modulo inverse is a^(m-2) mode m
        print("Modular multiplicative inverse is ",
              power(a, m - 2, m))

    # Driver code


print("Select operation.")
print("1.Euclid")
print("2.FLT")
print("3.")
print("4.Divide")
choice = 0
while choice != 6:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):

        if choice == '1':
            Euclid()

        elif choice == '2':
            a = input("Input a")
            m = input("Input mod")
            modInverse(a, m)

        break
    else:
        print("Invalid Input")