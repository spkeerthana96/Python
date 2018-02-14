def translate(str):
    l=['a','e','i','o','u']
    res=""
    for i in str:
        if (i in l)!=True and i.isalnum():
            res=res+i+"o"+i
        else:
            res=res+i
    print(res)
print("Enter a string")
str=input()
translate(str)