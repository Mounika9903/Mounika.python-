print("starting line")
a=[11,22,33]
print(a)

try:
   a=10/5
   print(a[5])
except:
    print("some exception raised")
else:
    print("no exception raised,everything worked properly")
finally:
     print("this is final block")
print("outside try block")




