age=27
if age<21:
    print("you cannot buy beer")
else:
    print("you can buy beer")

name="raghav"

if name is "raghav":
    print("the person is raghav")
elif name is "chetu":
    print("the person is chetanya")
else:
    print("hello world")
name=["raghav","chetu","ojas","chirag","popli","arsh"]
#loops
for f in name:
     print(f)
     print(len(f))
for f in name[0:3]:
    print("-->",f)
n =input("enter tyour name") 
print("hello",n)
#print 1--10
for x in range(11):
     print(x)
     print(name[x%6])
#print 3----12
for  x in range(3,13):
    print(x)
print(x)
# range(start,end,iterteration)
#print 2 iteration
for y in range(10,40,5):
    print(y)
