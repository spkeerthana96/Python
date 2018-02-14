def isvowel(val):
    ans=False
    l=['a','e','i','o','u']
    for i in l:
        if i==val:
            ans=True
    if(ans==True):
        print("%s is a vowel" % val)
    else:
        print("%s is not a vowel" % val)
isvowel('b')