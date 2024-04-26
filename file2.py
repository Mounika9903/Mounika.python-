fileObj1 = open("rollNumbers.txt", "w")
fileObj1.write("10 \n 20 \n 30 \n 40 \n 50 \n 60 \n 70 \n 80 \n 90 \n 100 \n")
fileObj1.close()
 
fileObj1 = open("rollNumbers.txt", "r")

print(fileObj1.readline())
print(fileObj1.readline())
print(fileObj1.readline())
print(fileObj1.readline())
fileObj1.close()
 
fileObj1 = open("rollNumbers.txt", "r")
fileObj2 = open("specialStudents.txt", "w")
fileObj1.readline()
fileObj2.write(fileObj1.readline())
fileObj2.write(fileObj1.readline())
fileObj2.write(fileObj1.readline())
fileObj2.write(fileObj1.readline())
fileObj2.write(fileObj1.readline())
 
 
fileObj1.close()
fileObj2.close()
 
fileObj1 = open("specialStudents.txt", "r")
print(fileObj1.read())
fileObj1.close()
 
fileObj1 = open("rollNumbers.txt", "r")
fileObj2 = open("otherStudents.txt", "w")
fileObj2.write(fileObj1.readline())
fileObj1.readline()
 
fileObj2.write(fileObj1.readline())
fileObj1.readline()
 
fileObj2.write(fileObj1.readline())
fileObj1.readline()
 
fileObj2.write(fileObj1.readline())
fileObj1.readline()
 
fileObj2.write(fileObj1.readline())
fileObj1.close()
fileObj2.close()
