#for i in range (5):
#    print(i)

#x = str(input("Enter a string: "))
#print("You entered: ", x)

#x=1024%11
#print(x)


i = 5

def f(arg=i):
    print(arg)

i = 6
f()

def fun():
    print('hello')

fun()

j=[]

def add(z):
    j.append(z)
    return j

print(add(1))
print(add(2))


