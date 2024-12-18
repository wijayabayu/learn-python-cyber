Nama_awal = "Muhammad"
Nama_tengah = "Dell"
Nama_Akhir = "Piero"

nama_lengkap = Nama_awal + " " + Nama_tengah + " " + Nama_Akhir 
print ("Jadi nama saya adalah", nama_lengkap)

panjangnama = len(nama_lengkap)
print ("jadi panjang hurufnya :", panjangnama)


M = "M"
status = M in nama_lengkap
print (M + " ada di " + nama_lengkap + " = " + str(status))

m = "m"
status = m not in nama_lengkap
print (m + " tidak ada di " + nama_lengkap + " = " + str(status))


a = "wk"
print (10*a)

print ("index ke-5 ="  + nama_lengkap[5])
print ("index ke-0-6 ="  + nama_lengkap[0:7])
print ("index ke-0,2,4,6,8 ="  + nama_lengkap[0:7:2])

print ("paling kecil",min(nama_lengkap))
print ("paling besar",max(nama_lengkap))

print (">>>>>>>>pemisah>>>>>>>>>>>>")
ascii_code = ord ("M")
print ("ASCI CODE untuk M adalah :"  + str(ascii_code))

data = 220
print ("Char untuk 117 adalah : " + chr(data))

namaorang = "Bayu Daya Wijaya"
jumlah = namaorang.count("y")
print ("Jumlah y pada namaorang adalah" +  namaorang + "=" +  str(jumlah))