print("starting line")
try:
   a=10/0
except:
    print("some exception raised")
else:
    print("no exception raised,everything worked properly")
finally:
     print("this is final block")
print("outside try block")



