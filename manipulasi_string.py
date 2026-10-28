nama ="Budi"
umur = 25

# cara yang salah (akan eror)
# pesan = "Nama saya" + nama + ", Umur " + umur

# cara yang benar
pesan= "Nama saya" + nama + ", Umur" + str(umur)
print(pesan)

print(len(nama))
print(len(pesan))

nama = "python"
print(nama[0])  # p (karakter pertama)
print(nama[1])  # y (karakter kedua)
print(nama[2])  # t (karakter ketiga)

nama =  "python"
print(nama[-1]) # n (karakter terakhir)
print(nama[-2]) # o (karakter kedua dari belakang)
print(nama[-3]) # h (karakter ketiga dari belakang)

nama = "python"
print(nama[0:3])    # pyt (index 0, 1, 2)
print(nama[2:5])    # tho (index 2, 3, 4)
print(nama[1:4])    # yth (index 1, 2, 3)

nama = "python"
print(nama[:3]) # pyt (dari awal sampai index 2)
print(nama[2:]) # thon (dari 2 sampai akhir)
print(nama)[:]  # python (seluruh string)

nama = "alice"
nama_upper = nama.upper()
print(nama_upper)   # ALICE
nama_lower = nama.lower()
print(nama_lower)   #alice

nama ="john doe"
nama_title = nama.title()
print(nama_title)   # John Doe
nama_capitalize = nama.capitalize()
print(nama_capitalize)  # John doe

nama = " Alice "
nama_strip = nama.strip()
print(nama_strip)   # 'Alice'

kalimat = "I love Java"
kalimat_baru = kalimat.replace("java", "Python")
print(kalimat_baru) # I love Python

nama = "Mississipi"
jumlah_s = nama.count("s")
print(jumlah_s) # 4

kalimat = "Belajar Python"
posisi = kalimat.find("Python")
print(posisi)   # 8

kalimat = "Baris pertama\nBaris kedua"
print(kalimat)

data = "Nama: \tAlice\n Umur: \t25"
print(data)

path = "C:\\Users\\hp\\Documents"
print(path)

kalimat1 = "Dia berkata \"Hello\" kepada saya"
print(kalimat1)

kalimat2 = 'I\'m learning python'
print(kalimat2)