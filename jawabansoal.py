def volume_balok(panjang,lebar,tinggi):
    volume = panjang*lebar*tinggi
    return volume

def volume_kubus(s):
    volume= s**3
    return volume


def volume_tabung(r,t):
    volume = 3.14*(r**2)*t
    return volume

print("===================== KALKULATOR CERDAS ==================")
print("Pililah bangun yang ingin anda hitung(inputan angka saja): ")
print("1. Tabung")
print("2. Kubus")
print("3. Balok")

pil = int(input("Masukan pilihan anda"))

if pil == 1:
    diameter = int(input("Masukan diameter(cm): "))
    tinggi = int(input("Masukan tinggi(cm):"))