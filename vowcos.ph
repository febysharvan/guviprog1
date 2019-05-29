a=input()
a.lower()
val=ord(a)
vow=['a','e','i','o','u']
if(val>95 and val<123):
   if a in vow:
       print("Vowel")
   else:
       print("Consonant")
else:
    print("invalid")
