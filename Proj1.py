import sys

n = 3

print("Arguments passed :",n)

print("File name :-",sys.argv[0])


  
# Getting the length of command
# line arguments

a = (sys.argv[1]).split("-")
b = (sys.argv[2]).split("-")
c = (sys.argv[3]).split("-")
print(a)    
print(b)
print(c)
h = 0
h1 = 0
h2 = 0
for i in range(0,len(a)):
    for j in range(0,len(c)):
        if a[i] == c[j]:
            h1 += 1
print(h1)
for i in range(0,len(a)):
    for j in range(0,len(c)):
        if b[i] == c[j]:
            h2 -= 1
print(h2)

h = h1-h2
print(h)


