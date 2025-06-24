a = int(input("A: "))
b = int(input("B: 5" "))
print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
try:
    result = a/b
except ZeroDivisionError:
    result = None
    print("a/b=",result)
    print("cannot divded by zerro")