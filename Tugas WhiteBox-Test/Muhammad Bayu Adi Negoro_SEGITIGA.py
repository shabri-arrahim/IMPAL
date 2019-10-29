#Latihan di Kelas (IMPAL)
#SEGITIGA
#MUHAMMAD BAYU ADI N
#1301170762
#IFIK-41-03
import math

#Dari masukan 3 bilangan a,b,c bebas segitiga apa dapat dibangun.
a = float (input("masukan bilangan a : "))
b = float (input("masukan bilangan b : "))
c = float (input("masukan bilangan c : "))

#mencari bilangan yang terbesar
BB = max([a,b,c])
#penjumlahan a dan b
jumAB = a+b
#penjumlahan b dan c
jumBC = b+c
#penjumlahan c dan a
jumCA = c+a
#penjumlahan kuadrad a dan b
jumkuadradAB = (a**2)+(b**2)
#penjumlahan kuadrad b dan c
jumkuadradBC = (b**2)+(c**2)
#penjumlahan kuadrad c dan a
jumkuadradCA = (c**2)+(a**2)

#Jika ada yang negatif atau0, tidak ada segitiga dapat dibangun.
if ((a<=0) or (b<=0) or (c<=0)):
	print ("Tidak Ada Segitiga Dapat Di Bangun")
#Jika a=b dan b=c maka segitiga SAMA SISI.
elif ((a==b) and (b==c)):
	print ("segitiga SAMA SISI")
#Jika bilangan yang terbesar lebih besar atau sama dengan penjumlahan dua bilangan lainnya yang lebih kecil, tidak ada segitiga dapat dibangun
elif ((BB>=jumAB) or (BB>=jumBC) or (BB>=jumCA)):
	print ("Tidak Ada Segitiga Dapat Di Bangun")
#Jika a=b atau b=c atau a=c (namun tidak sama dengan salah satu yang lain maka segitiga SAMA KAKI.
elif ((a==b) or (b==c) or (c==a)):
	print ("segitiga SAMA KAKI")
#Jika kuadrat bilangan terbesar = penjumlahan dari kuadrat dua bilangan lainnya, maka SEGITIGA SIKU-SIKU. 
elif ((BB**2==jumAB) or (BB**2==jumBC) or (BB**2==jumCA)):
	print ("segitiga SIKU-SIKU")
#Jika bukan sama kaki, sama sisi atau siku-siku, namun bilangan terbesarnya lebih kecil daripada penjumlahan dua bilangan lainnya, maka SEGITIGA BEBAS. 
elif ((BB<jumAB) or (BB<jumBC) or (BB<jumCA)):
	print ("segitiga SEMBARANG")
