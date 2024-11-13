# Python-Loop Project
# Created by: SlaX0riuZ
# 11/13/2024
# v0.0.01 Alpha

'''
For Extra "Creativity Points":
- Possibly implement A x 10^B notation for anything over 10^10
- Use try/except/else/finally
'''


print("Python-Loop Factorial Calculator")
print("Created by SlaX0riuZ")
print("<------------------------->")

try: # Give user something to input
    unum = int(input("Input the number you want to take a factorial of: "))

except ValueError: # User didn't input an integer.
    print("Please input a number that's an integer.")

else: # User inputted an integer.

    def get_fct(n): # Factorial Calculator's basic function
        z = 1
        for i in range(n, 1, -1):
            z = z * i
        return z

    output = "" # Giving the computer something to edit.

    if unum < 0: # Prevent Negative Factorial Error...
        print("Error! Negative factorial numbers don't exist.")
        print("Please input a number that's greater than or equal to 0.")
        print("<------------------------->")
    else:
        output = str(get_fct(unum))
        
        if len(output) >= 10: # Use Scientific Notation
            v_exp = int(len(output)) - 1
            v_front = str(output[:1]) + "." + str(output[1:4])
            print(str(unum) + "! is: " + str(v_front) + " x 10^" + str(v_exp))

        else: # No need to use Scientific Notation
            print(str(unum) + "! is: " + str(output))