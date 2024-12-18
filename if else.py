print("masukkan nilai yang anka berpuluhan")
grade = float(input("Masukkan Nilai Kamu :\t"))

if grade >= 80:
    print("Nilai Kamu adalah A")
elif grade >= 70:
    print("Nilai Kamu adalah B")
elif grade >= 60:
    print("Nilai Kamu adalah C")
else:
    print("Makanya lebih giat belajarnya -_-")

print("Catatan : Jangan memasukkan nama lebih dari 5 huruf")
name = str(input("Masukkan nama kamu :\t"))
if len(name) < 6 :
    print("Cek nama yang dimasukkan :\t", name)
else:
    print ("Namanya kepanjangan bang :)")