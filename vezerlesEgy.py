import random
"""
for i in range(2,10):
    print(i)

for i in range(2,10,2):
    print(i)

A = [1, 2, 3, 4, 5]
 
for i in range(len(A)):
    print(A[i])

s = 0
for i in range(10):
    v = random.randint(1,6)
    s += v
    print(i+1, v)
print(s)

db = 0
for i in range(6000):
    v = random.randint(1,6)
    if v == 6:
        db += 1

print("6-osok száma: ",db)


db = [0, 0, 0, 0, 0, 0]

for i in range(6000):
    v = random.randint(1, 6)
    db[v-1] += 1
print(db)

db = [0, 0, 0, 0, 0, 0]

i = 0
while i < 600000:
    v = random.randint(1,6)
    db[v-1] += 1
    i += 1
print(db)

a = []

# 4.

for i in range(14):
    v = random.randint(1,3)
    if v  == 3:
        a.append("X")
    else:
        a.append(v)
print(a)
"""

eves = int(input("Hány éves? "))
print(eves*"Boldog szülinapot!\n")