# Python-Loop Project
# Created by: SlaX0riuZ
# 11/13/2024
# v0.0.01 Alpha
#updated 10:46 AM

'''
For Extra "Creativity Points":
- Allow float values for factorials!
- Possibly implement A x 10^B notation for anything over 10^10
'''


print("Python-Loop Factorial Calculator")
print("Created by SlaX0riuZ")
print("<------------------------->")


unum = int(input("Input the number you want to take a factorial of: "))


def get_fct(n):
    z = 1 # temporary variable
    for i in range(n, 1, -1):
        z = z * i
    return z


output = get_fct(unum)
print(output)