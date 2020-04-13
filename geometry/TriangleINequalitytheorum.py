print("What is A")
a = input()
a = float(a)
print("What is B")
b = input()
b = float(b)
print("What is C")
c = input()
c = float(c)


if a + b > c:
    print("Pass One")
else:
    print("Fail One ")
    exit(1)

if a + c > b:
    print("Pass Two")
else:
    print("Fail Two ")
    exit(1)

if b + c  > a:
    print("Pass Three")
else:
    print("Fail Three ")
    exit(1)