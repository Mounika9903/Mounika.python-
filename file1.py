 fileObj1 = open("names.txt", "w")
    fileObj1.write("raj \n kiran \n vaishu \n Krishna")
    fileObj1.close()
 
    fileObj1 = open("names.txt", "r")
    print(fileObj1.read())
    fileObj1.close()
 
    fileObj1 = open("names.txt", "r")
    fileObj2 = open("newNames.txt", "w")
    fileObj2.write(fileObj1.read())
    fileObj1.close()
    fileObj2.close()
 
    fileObj1 = open("newNames.txt", "r")
    print(fileObj1.read())
 
