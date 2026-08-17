a=float(input("enter first number:"))
b=float(input("enter second number:"))
c=float(input("enter third number:"))

if a>=b:
    if a>=c:
        largest=a
    else:
        largest=c
else:
    if b>=c:
        largest=b
    else:
        largest=c

print("largest number:",largest)
