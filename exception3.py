print("starting line")
a=[11,22,33]
try:
    print(a[5])
    a=10/0
    
except ZeroDivisionError:
    print("Exception raised due to zero division error")
except IndexError:
     print("Exception raised due to index out of range")  
except NameError:
         print("Exception raised due to undefined variable")
except:
    print("some exception raised")
else:
    print("no exception raised,everything worked properly")
finally:
     print("this is final block")
print("outside try block")

