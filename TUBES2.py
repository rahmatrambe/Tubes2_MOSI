import random
from random import choices
### ~~~~~ Menyiapkan Variabel ~~~~~ ###
jum_indiv = 200
infected = jum_indiv * 5/100
waktu_pemulihan = 9  # Karena python dimulai dari 0, sehingga sama saja dengan 10
x_max,y_max = 20,20
x_min,y_min = 0,0
probability = 0.8
total_pemulihan_komunitas = 1
posx,posy = [],[]
posxInfected,posyInfected = [],[]
kesehatan = []
imunitas = []
infectedtime = []
### ~~~~~ Data 200 Individu ~~~~~ ###
virus = 0
i = 0
while virus <infected or i<jum_indiv:
    x = random.randint(x_min,x_max)
    y = random.randint(y_min,y_max)
    posx.append(x)
    posy.append(y)
    if virus <= 9:
        kesehatan.append("terinfeksi")
        imunitas.append("belum_imun")
        infectedtime.append(1)
        virus+=1
    else:
        kesehatan.append("belum_terinfeksi")
        imunitas.append("belum_imun")
        infectedtime.append(0)
    i+=1
### Mencatat titik koordinat yang terinfeksi ###
for i in range(jum_indiv):
    if kesehatan[i] == "terinfeksi":
        posxInfected.append(posx[i])
        posyInfected.append(posy[i])
### Membuat Fungsi PBC ###
def PBCx(x):
    if x > x_max:
        x += -x_max
    if x < x_min:
        x += +x_max
    return x
def PBCy(y):
    if y > y_max:
        y += -y_max
    if y < y_min:
        y += +y_max
    return y
totalinfected = virus
totalsembuh = 0
while totalsembuh != totalinfected: #Akan loop sampai semua yang terinfeksi sembuh
    for i in range(jum_indiv):
        x = [0,1]
        weights = [probability,.2]
        b = random.choices(x,weights) #Random Probability
        if b[0] == 0: #Jika individu bergerak
            nilai = random.uniform(0,1)
            if nilai <= 0.25:
                posx[i]=posx[i]+1
                posx[i]=PBCx(posx[i])
            elif nilai <= 0.50:
                posy[i]=posy[i]-1
                posy[i]=PBCy(posx[y])
            elif nilai <= 0.75:
                posx[i]=posx[i]-1
                posx[i]=PBCx(posx[i])
            else:
                posy[i]=posy[i]+1
                posy[i]=PBCy(posx[y])
        if kesehatan[i] == "terinfeksi": ### Jika individu terinfeksi, maka di cek infected time nya sudah berapa lama#
            infectedtime[i] = infectedtime[i]+1
            total_pemulihan_komunitas = total_pemulihan_komunitas + 1
            if infectedtime[i] >= waktu_pemulihan: ### Jika sudah 10 Hari, maka dinyatakan pulih dan imun menjadi kebal
                kesehatan[i] = "pulih"
                imunitas[i] = "kuat"
                if not posxInfected:
                    print("abis")
                else:
                    posxInfected.pop(0)
                    posyInfected.pop(0)
        for j in range(len(posxInfected)):
            if posx[i]==posxInfected[j] and posy[i]==posyInfected[j]: ### Melakukan perbandingan jarak terinfeksi dan non terinfeksi
                if totalinfected < jum_indiv and kesehatan[i] == "belum_terinfeksi": # Jika individu masih blm terinfeksi, maka dia tertular
                    kesehatan[i] = "terinfeksi"
                    totalinfected = totalinfected + 1 ##Bertambahnya individu yang tertular corona
                    posxInfected.append(posx[i])
                    posyInfected.append(posy[i])
    totalsembuh = totalsembuh + 1
print("Total Sembuh              :",totalsembuh)
print("Total Infected            :",totalinfected)
print("Total Pemulihan Komunitas :",total_pemulihan_komunitas,"Hari")
