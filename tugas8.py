data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# 1.Tampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing.
for i, j in data_panen.items():
    print(i, j)
print()
# 2.Tampilkan jumlah hasil panen jagung dari lokasi2.
print(data_panen["lokasi2"]["hasil_panen"]["jagung"])
print()
# 3.Tampilkan nama lokasi dari lokasi3.
print(data_panen["lokasi3"]["nama_lokasi"])
print()
# 4 dan 5.Masukkan Jumlah Hasil Panen Padi dan Kedelai Setiap Lokasi ke Dalam Variabel yang Berbeda
jmlhPadi = []
jmlhkedelai = []
jmlhJagung = []
for i, j in data_panen.items():
    jmlhPadi.append(j["hasil_panen"]["padi"])
    jmlhkedelai.append(j["hasil_panen"]["kedelai"])
    jmlhJagung.append(j["hasil_panen"]["jagung"])
print(jmlhPadi)
print(jmlhkedelai)
print()
# 6.Buat Percabangan Jika jumlah hasil panen padi lebih dari 1300 atau jagung lebih dari 800 di suatu lokasi, maka lokasi tersebut memerlukan perhatian khusus.Jika tidak, maka lokasi tersebut dalam kondisi baik.
for i in range(len(jmlhJagung)):
    if jmlhPadi[i] > 1300 or jmlhJagung[i] > 800:
        print(f"maka lokasi {i+1} tersebut memerlukan perhatian khusus")
    else:
        print(f"maka lokasi {i+1} tersebut dalam kondisi baik.")

print("saya manusia")
