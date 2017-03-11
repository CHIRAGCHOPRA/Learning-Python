fileObject=open("testFile.txt",'w')
fileObject.write('this is test text\n testing file is this')
fileObject.close()

fileObject1 = open("testFile.txt",'r')

string=fileObject1.read()
print(string)
