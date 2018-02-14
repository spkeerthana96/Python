def max_of_three(a,b,c):

    if a>b and a>c:

        return a

    elif b>c:

        return b

    else:
        return c
print("Enter 1st number")
a=input()

print("Enter 2nd number")
b=input()
print("Enter 3rd number")

c=input()
d=max_of_three(int(a),int(b),int(c))

print("Maximum among "+a+","+b+","+c+" is",d)