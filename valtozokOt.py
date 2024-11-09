# 5. feladat Kérjünk be két számot úgy, hogy később matematikai műveleteket tudjunk
# rá alkalmazni. Ezek lesznek egy téglalap oldalai. Írassuk ki a területét, kerületét a kiírás
# mellé és alá

a = int(input("Kérem az a oldal hosszát! "))
b = int(input("Kérem a b oldal hosszát! "))

k = 2*(a+b)
t = (a*b)

print("A téglalap kerülete: ", str(k))
print("A téglalap kerülete: ", k)
print("A téglalap kerülete: ", end='')
print(k)

print("A téglalap területe: ", t)
print("A téglalap területe: ", t, sep='\n')
print("A téglalap területe: ", t,t,t, sep='\n')
     
      
""""
a = int(input("Please input edge 1 (cm): "))
b = int(input("Please input edge 2 (cm): "))

area = a * b

perimeter = 2 * (a + b)

print(2* (f"The perimeter of the rectangle is: " + str(perimeter) + "cm\n"))
print("The perimeter of the rectangle is: ", str(perimeter), sep='\n')
"""

