def maximum(a,b):

    if a>b:

        return a

    else:

        return b

a=input()

b=input()

c=maximum(int(a),int(b))

print("Maximum among "+a+" and "+b+" is "+str(c))