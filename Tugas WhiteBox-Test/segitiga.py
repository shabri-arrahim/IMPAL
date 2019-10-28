segitiga = []
i = 1
max = 0
pointmax = 0
while(i <= 3):
	a = float(input("Masukkan angka ke-%d : "%(i)))
	if(a > 0):
		segitiga.append(a)
		if(segitiga[i-1]>max):
			max = segitiga[i-1]
			pointmax = i-1
	else:
		print("wrong input")
		break
	i+=1
print('Pointmax: ',pointmax, ' Max: ',max)

if(len(segitiga) == 3):
	if(pointmax==2):
		if((segitiga[pointmax-1]+segitiga[pointmax-2]) == max):
			print("wrong dimension1")
		elif(segitiga[pointmax-1]==segitiga[pointmax-2]):
			print("Segitiga Sama Kaki")
		elif(segitiga[pointmax]**2 == segitiga[pointmax-1]**2+segitiga[pointmax-2]**2):
			print("Segitiga Siku-Siku")
		elif(segitiga[pointmax-1]+segitiga[pointmax-2]>segitiga[pointmax]):
			print("Segitiga Bebas")
		else:
			print("Tidak ada segitiga yang terdefinisi")
	elif(pointmax==0):
		if((segitiga[pointmax+1]+segitiga[pointmax+2]) == max):
			print("wrong dimension2")
		elif(segitiga[pointmax+1]==segitiga[pointmax+2] and segitiga[pointmax]!=segitiga[pointmax+1]):
			print("Segitiga Sama Kaki")
		elif(segitiga[pointmax]==segitiga[pointmax+2] and segitiga[pointmax] != segitiga[pointmax+1]):
			print("segitiga Sama Kaki")
		elif((segitiga[pointmax+1]==segitiga[pointmax+2]) and (segitiga[pointmax]==segitiga[pointmax+1])):
			print("Segitiga Sama Sisi")
		elif(segitiga[pointmax]**2==segitiga[pointmax+1]**2+segitiga[pointmax+2]**2):
			print("Segitiga Siku-siku")
		elif(segitiga[pointmax+1]+segitiga[pointmax+2]>segitiga[pointmax]):
			print("segitiga Bebas")
		else:
			print("Tidak ada segitiga yang terdefinisi")
	else:
		if((segitiga[pointmax-1]+segitiga[pointmax+1]) == max):
			print("wrong dimension3")
		elif(segitiga[pointmax]==segitiga[pointmax+1] or (segitiga[pointmax-1]==segitiga[pointmax+1] 
			and segitiga[pointmax] != segitiga[pointmax-1])):
			print("Segitiga Sama Kaki")
		elif(segitiga[pointmax]**2 == segitiga[pointmax-1]**2+segitiga[pointmax+1]**2):
			print("Segitiga Siku-Siku")
		elif(segitiga[pointmax-1]+segitiga[pointmax+1]>segitiga[pointmax]):
			print("Segitiga Bebas")
		else:
			print("Tidak ada segitiga yang terdefinisi")
