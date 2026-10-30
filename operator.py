a = 10
b = 3

print(a + b)    # Penjumlahan: 13
print(a - b)    # Pengurangan: 7
print(a * b)    # Perkalian: 30
print(a / b)    # Pembagian: 3.333...

print(a // b)   # Pembagian bulat: 3 (hasil tanpa desimal)
print(a % b)    # Modulo: 1 (sisa pembagian)

# Contoh praktis modulo
print(10 % 2)   # 0 (10 habis di bagi 2)
print(11 % 2)   # 1 (sisa 1 ketika 11 dibagi 2)

a = 2
b = 3

print(a ** b)   # Pangkat: 8 (2 pangkat 3)

# Contoh lain
print(5 ** 2)   # 25 (5 pangkat 2)
print(3 ** 4)   # 81 (3 pangkat 4)

x = 10
print("x awal:", x)

x += 5  # Sama dengan: x = x + 5
print("x setelah += 5:", x) # 15

x -= 3  # Sama dengan: x = x - 3
print("x setelah -= 3:", x) # 12

x *= 2  # Sama dengan: x = x * 2
print("x setelah *= 2", x)  # 24

x /= 4 # Sama dengan: x = x / 4
print("X setelah /= 4", x)  # 6.0

print(a > b)    # Lebih besar: True
print(a < b)    # Lebih kecil: False
print(a >= b)   # Lebih besar atau sama: True
print(a <= b)   # Lebih kecil atau sama: False
print(a == b)   # Sama dengan: False
print(a != b)   # Tidak sama dengan: False

nama1 = "Alice"
nama2 = "Bob"
nama3 = "Alice"

print(nama1 == nama3)   # True
print(nama1 == nama2)   # False
print(nama1 != nama2)   # True