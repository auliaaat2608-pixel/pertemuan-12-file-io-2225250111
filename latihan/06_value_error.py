try:
    nilai = input("Masukkan nilai: ")
    nilai = float(nilai)

    print("Nilai yang dimasukkan:", nilai)

except ValueError:
    print("Error: Masukkan angka yang valid.")