a = input("-,+,*,/ :")
condition_1 = ("-")
condition_2 = ("+")
condition_3 = ("/")
condition_4 = ("*")
if a == condition_1:
    c = int(input("enter large value:"))
    d = int(input("enter second value:"))
    minus = lambda x,y:x-y
    print(minus(c,d))
if a == condition_2:
    e = int(input("enter first value:"))
    f = int(input("enter second value:"))
    add = lambda x,y:x+y
    print(add(e,f))

if a == condition_3:
    g = int(input("enter numerator:"))
    h = int(input("enter denominator:"))
    div = lambda x,y: x/y
    print(div(g,h))
if a == condition_4:
    j = int(input("enter first value:"))
    k = int(input("enter second value:"))
    multiply = lambda x,y : x*y
    print(multiply(j,k))

else:
    print("enter a valid operation")
