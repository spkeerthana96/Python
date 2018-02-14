def max_of_three(a,b,c):

    if a>b and a>c:

        return a

    elif b>c:

        return b

    else:
        return c
a=input()

b=input()

c=input()
d=max_of_three(int(a),int(b),int(c))

print("Maximum among "+a+","+b+","+c+" is "+str(d))