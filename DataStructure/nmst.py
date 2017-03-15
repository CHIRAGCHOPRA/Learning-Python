
def f(x):
    return (1-x*x)**(0.5)

array_of_x=list()
array_of_y=list()
a=float(input("value of a"))
b=float(input("value of b"))
n=int(input("value of n"))

h=(b-a)/n
n+=1
print("h=",h)
for i in range(n):
    c=a+(h*i)
    array_of_x.append(c)
    array_of_y.append(f(c))
ans=array_of_y[0]+array_of_y[n-1]
even=0
odd=0
for i in range(1,n-1):
    if(i%2==0):
        even+=2*array_of_y[i]
    else:
        odd+=4*array_of_y[i]
ans+=odd+even
print(even)
print(odd)
ans=(ans*h)/3
print(ans)
    
