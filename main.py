"""

A	=	final amountP	=	initial principal balance

r	=	interest rate

n	=	number of times interest applied per time period

t	=	number of time periods elapsed

"""

from time import sleep

p = (input("Enter initial amount:"))

r = input("Enter interest rate:")

n = input("Enter number of times interested should be applied:")

t = input("Enter number of periods:")

  

try:

    p = int(p)

    r = int(r)

    n = int(n)

    t = int(t)

except ValueError:

    p = float(p)

    r = float(r)

    n = float(n)

    t = float(t)

except Exception:

    print("Enter a number or decimal")

else:

    print("calculating..............")

  

"""

FORMULA

 p * (pow((1 + r / 100), t))

 """

 

r = r/100

a = p * (pow((1 + r/n), n*t))

sleep(7)

print(a)

 



