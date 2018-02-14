def maximum(a,b):

    if a>b:

        return a

    else:

        return b


print("Enter 1st number")
a=input()

print("Enter 2nd number")
b=input()

c=maximum(int(a),int(b))

print("Maximum among "+a+" and "+b+" is",c)