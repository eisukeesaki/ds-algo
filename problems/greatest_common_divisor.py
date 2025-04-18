import math

# def gcd(num1, num2):
#     if num1 == num2:
#         return num1
#     if num1 < num2:
#         tmp = num1
#         num1 = num2
#         num2 = tmp
#     while num1 % num2 != 0:
#         r = num1 % num2
#         num1 = num2
#         num2 = r
#     return r

# def gcd_rec(num1, num2):
#     if num1 == num2:
#         return num2
#     if num1 < num2:
#         tmp = num1
#         num1 = num2
#         num2 = tmp
#     if num1 % num2 == 0:
#         return num2
#     return gcd_rec(num2, num1 % num2)

def gcd(num1, num2):
    if num1 == num2:
        return num2
    if num1 > num2:
        return gcd(num1 - num2, num2)
    if num2 > num1:
        return gcd(num2 - num1, num1)

a = -3
b = -8
if math.gcd(a, b) == gcd(a, b):
    print("OK")
else:
    print(f"math:{math.gcd(a, b)}")
    print(f"custom:{gcd(a, b)}")
