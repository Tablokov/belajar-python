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