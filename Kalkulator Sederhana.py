print(30*"=")
print("Kalkulator Sederhana")
print(30*"=")
catatan = "+ : tambah\n- : pengurangan\n* : perkalian\n/ : pembagian"
print(catatan)


progam_1 = float(input("Masukkan angka ke 1 : "))
operator_tersedia = input("Masukkan operator yang diinginkan (+,-,*,/) : ")
progam_2 = float(input("Masukkan angka ke 2 : "))

if operator_tersedia == "+":
    hasil = progam_1 + progam_2
    print(f"Hasilnya adalah : {hasil}")

elif operator_tersedia == "-":
    hasil = progam_1 - progam_2
    print(f"Hasilnya adalah : {hasil}")

elif operator_tersedia == "*" or operator_tersedia == "x":
    hasil = progam_1 * progam_2
    print(f"Hasilnya adalah : {hasil}")

elif operator_tersedia == "/":
    hasil = progam_1 / progam_2
    print(f"Hasilnya adalah : {hasil}")

else:
    print("Masukkan Progam atau Operator Yang Valid")

