# Masukan nilai
r = input("Masukan jari-jari lingkaran : ")

# Mendeklarasikan nilai phi
pi = 3.14

# Masukan Rumus luas dan keliling lingkaran
l = pi * int (r) * int (r)
k = 2 * pi * int(r)

# Cetak hasil perhitungan
print("Luas lingkaran = ","{:.2f}".format(l))
print("Keliling lingkaran = ","{:.2f}".format(k)) 